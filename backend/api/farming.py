from flask import Blueprint, request, jsonify
import requests
import random
from backend.utils.ai_helper import call_groq_ai
from backend.utils.constants import CROP_INFO

farming_bp = Blueprint('farming', __name__)

@farming_bp.route('/ai-location')
def ai_location():
    lat, lon = request.args.get('lat', '28.6139'), request.args.get('lon', '77.2090')
    try:
        geo = requests.get(f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}", headers={'User-Agent': 'Agrinova'}, timeout=3).json()
        raw = geo.get('display_name', 'Unknown')
    except: raw = f"Lat:{lat}, Lon:{lon}"
    prompt = f"Analyze location for farming: {raw}. Provide farmer friendly address, agricultural zone, soil type, and major crops in JSON: {{address: '', zone: '', soil: '', crops: []}}"
    return jsonify(call_groq_ai(prompt) or {"address": raw, "zone": "Active Farm Land", "soil": "Alluvial", "crops": ["Wheat", "Rice"]})

@farming_bp.route('/calculate-yield-ai', methods=['POST'])
def calculate_yield_ai():
    d = request.json
    prompt = f"Calculate yield, revenue, cost, profit for {d}. JSON: {{yield_qty: 0, revenue: 0, cost: 0, profit: 0, analysis: '', yield_boosters: [], cost_tips: []}}"
    return jsonify(call_groq_ai(prompt) or {"yield_qty": 100, "revenue": 200000, "cost": 50000, "profit": 150000, "analysis": "High potential.", "yield_boosters": ["NPK management"], "cost_tips": ["Solar pumps"]})

@farming_bp.route('/recommend-crop', methods=['POST'])
def recommend_crop():
    data = request.json or {}
    prompt = f"""You are an elite agricultural decision support system. 
    REALISM is your priority. If factors mismatch, you must be honest.
    
    CRITICAL RULES:
    1. DO NOT give high confidence if ANY major factor mismatches: Soil, Climate, Water.
    2. If mismatch: Reduce confidence, mark as "Conditional", clearly explain why.
    3. PRIORITIZE: Soil compatibility > Climate > Water > Season.
    4. If soil is NOT suitable: Suggest better alternatives, do NOT rank as Best Match.
    
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
