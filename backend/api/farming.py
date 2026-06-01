from flask import Blueprint, request, jsonify
import requests
from backend.config import Config
from backend.utils.ai_helper import call_groq_ai
from backend.utils.constants import CROP_INFO

farming_bp = Blueprint('farming', __name__)

BASE_YIELD = {
    'wheat': 25,
    'rice': 28,
    'maize': 30,
    'cotton': 12,
    'soybean': 15,
    'sugarcane': 350,
    'tomato': 120,
    'potato': 100
}


def reverse_geocode(lat, lon):
    try:
        resp = requests.get(
            Config.NOMINATIM_URL,
            params={"format": "json", "lat": lat, "lon": lon},
            headers={"User-Agent": "Agrinova"},
            timeout=5
        )
        resp.raise_for_status()
        geo = resp.json()
        return geo.get('display_name') or f"Lat:{lat}, Lon:{lon}"
    except Exception:
        return f"Lat:{lat}, Lon:{lon}"


def fetch_crop_yield_data(crop_name=None, state=None, district=None):
    if not Config.DATA_GOV_API_KEY:
        return []

    params = [
        ("api-key", Config.DATA_GOV_API_KEY),
        ("format", "json"),
        ("limit", "5")
    ]
    if crop_name:
        params.append(("filters[commodity_name]", crop_name))
    if state:
        params.append(("filters[state_name]", state))
    if district:
        params.append(("filters[district_name]", district))

    try:
        resp = requests.get(Config.CROP_YIELD_URL, params=params, timeout=10)
        resp.raise_for_status()
        payload = resp.json()
        return payload.get('records') or payload.get('data') or []
    except Exception:
        return []


@farming_bp.route('/ai-location')
def ai_location():
    lat, lon = request.args.get('lat', '28.6139'), request.args.get('lon', '77.2090')
    raw = reverse_geocode(lat, lon)
    prompt = f"Analyze location for farming: {raw}. Provide farmer friendly address, agricultural zone, soil type, and major crops in JSON: {{address: '', zone: '', soil: '', crops: []}}"
    return jsonify(call_groq_ai(prompt) or {"address": raw, "zone": "Active Farm Land", "soil": "Alluvial", "crops": ["Wheat", "Rice"]})


@farming_bp.route('/calculate-yield-ai', methods=['POST'])
def calculate_yield_ai():
    d = request.json or {}
    crop_name = (d.get('crop_name') or d.get('crop') or d.get('commodity') or '').lower()
    area = float(d.get('area', 1) or 1)
    price = float(d.get('price', 2000) or 2000)
    input_cost = float(d.get('cost', 8000) or 8000)

    try:
        soil_factor = float(d.get('soil', 1.0))
    except Exception:
        soil_factor = 1.0
    try:
        irr_factor = float(d.get('irr', 1.0))
    except Exception:
        irr_factor = 1.0

    base_yield = BASE_YIELD.get(crop_name, 20)
    yield_qty = round(base_yield * area * soil_factor * irr_factor, 1)
    revenue = round(yield_qty * price)
    cost = round(input_cost * area)
    profit = revenue - cost

    baseline = fetch_crop_yield_data(crop_name=crop_name, state=d.get('state'), district=d.get('district'))
    baseline_note = ''
    if baseline:
        baseline_note = f"Use baselines from official crop yield data when calculating expectations. Records: {baseline[:3]}"

    prompt = f"Provide farming insight for {crop_name} with {yield_qty} qtl from {area} acres, price {price} ₹/qtl, input cost {input_cost} ₹/acre, soil factor {soil_factor}, irrigation factor {irr_factor}. {baseline_note} Return JSON: {{analysis: '', yield_boosters: [], cost_tips: []}}"
    ai_response = call_groq_ai(prompt)

    analysis = {
        'yield_qty': yield_qty,
        'revenue': revenue,
        'cost': cost,
        'profit': profit,
        'analysis': ai_response.get('analysis') if isinstance(ai_response, dict) and ai_response.get('analysis') else 'Calculated using crop-specific yield factors and input costs.',
        'yield_boosters': ai_response.get('yield_boosters') if isinstance(ai_response, dict) and ai_response.get('yield_boosters') else ['Use balanced NPK fertilizer', 'Adopt timely irrigation', 'Monitor pest pressure regularly'],
        'cost_tips': ai_response.get('cost_tips') if isinstance(ai_response, dict) and ai_response.get('cost_tips') else ['Use efficient irrigation to save water', 'Switch to bulk seed procurement to lower input cost']
    }
    if baseline:
        analysis['baseline_crop_yield_records'] = baseline[:3]
    return jsonify(analysis)


@farming_bp.route('/recommend-crop', methods=['POST'])
def recommend_crop():
    data = request.json or {}
    try:
        ph_value = float(data.get('ph', 0))
    except Exception:
        return jsonify({"success": False, "error": "Please enter a valid soil pH value between 1 and 7."}), 400
    if ph_value < 1 or ph_value > 7:
        return jsonify({"success": False, "error": "Please enter a valid soil pH value between 1 and 7."}), 400
    data['ph'] = ph_value
    prompt = f"""You are an elite agricultural decision support system. 
    REALISM is your priority. If factors mismatch, you must be honest.
    
    CRITICAL RULES:
    1. DO NOT give high confidence if ANY major factor mismatches: Soil, Climate, Water.
    2. If mismatch: Reduce confidence, mark as \"Conditional\", clearly explain why.
    3. PRIORITIZE: Soil compatibility > Climate > Water > Season.
    4. If soil is NOT suitable: Suggest better alternatives, do NOT rank as Best Match.
    5. ONLY accept soil pH values between 3.5 and 9.5. If the provided pH is out of range, return an error message.
    
    INPUT DATA:
    - Soil Type: {data.get('soil_type')}
    - ph: {data.get('ph')}
    - Temperature: {data.get('temperature')}°C
    - Humidity: {data.get('humidity')}%
    - Rainfall: {data.get('rainfall')}mm
    - Water Source: {data.get('water_source')}
    - Location: {data.get('location')}
    - Season/Month: {data.get('sowing_month')}
    - Field Notes: {data.get('field_notes')}

    STRICT JSON OUTPUT ONLY:
    {{
      "primary_recommendation": {{
        "crop": "Crop Name",
        "confidence": "X%",
        "recommendation_type": "Best" or "Conditional",
        "reason_summary": "Short explanation",
        "issues_detected": ["Problem 1"],
        "yield_estimate": "X tons/ha",
        "profit_estimate": "₹X - ₹Y",
        "duration": "X days",
        "risk_level": "Low/Medium/High"
      }},
      "suitability_scores": {{
        "soil_match": "X%",
        "climate_match": "Y%",
        "water_match": "Z%"
      }},
      "detailed_analysis": {{
        "why_this_crop": ["Reason 1"],
        "limitations": ["Risk 1"],
        "action_plan": ["Step 1"],
        "fertilizer_plan": ["N-P-K context"],
        "irrigation_plan": ["Method"]
      }},
      "alternative_crops": [
        {{"crop": "Alt1", "reason": "Why better for soil", "expected_profit": "₹X", "risk_level": "Low"}}
      ],
      "alerts": ["Alert text"]
    }}"""
    analysis = call_groq_ai(prompt) or {
        "primary_recommendation": {
            "crop": "Wheat", "confidence": "70%", "recommendation_type": "Conditional", 
            "reason_summary": "System offline fallback", "issues_detected": ["Manual override active"],
            "yield_estimate": "4 tons/ha", "profit_estimate": "₹50k", "duration": "120 days", "risk_level": "Medium"
        },
        "suitability_scores": {"soil_match": "60%", "climate_match": "80%", "water_match": "70%"},
        "detailed_analysis": {"why_this_crop": [], "limitations": [], "action_plan": [], "fertilizer_plan": [], "irrigation_plan": []},
        "alternative_crops": [], "alerts": []
    }
    
    crop_name = analysis.get('primary_recommendation', {}).get('crop', 'Wheat')
    info = CROP_INFO.get(crop_name.lower())
    if not info:
        for k, v in CROP_INFO.items():
            if k in crop_name.lower(): 
                info = v
                break
    analysis['primary_recommendation']['icon'] = info['icon'] if info else '🌱'
    
    return jsonify({"success": True, "data": analysis})


@farming_bp.route('/simplify-recommendation', methods=['POST'])
def simplify_recommendation():
    d = request.json
    prompt = f"Simplify this agricultural advice for a farmer in plain language. Original: {d}. JSON: {{simple_explanation: ''}}"
    return jsonify(call_groq_ai(prompt) or {"simple_explanation": "This crop is great for your soil. Plant it soon for best results."})
