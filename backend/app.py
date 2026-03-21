"""
Agrinova - AI Powered Farming Assistant
Created by Parth Dahiphale
Uses Groq & Gemini AI for accurate farming insights
"""

import os
import requests
import json
import random
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import sys
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', stream=sys.stdout)

app = Flask(__name__, static_folder='../frontend', template_folder='../frontend', static_url_path='')
app.config['SECRET_KEY'] = 'agrinova-secret-key-parth-2026'
CORS(app)

# Fetch API Key from environment variable for security
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def call_groq_ai(prompt, model="llama-3.3-70b-versatile"):
    api_key = os.environ.get('GROQ_API_KEY', GROQ_API_KEY)
    if not api_key:
        print("⚠️ Error: GROQ_API_KEY not found in environment.")
        return None
    try:
        response = requests.post(GROQ_API_URL, headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json={"model": model, "messages": [{"role": "user", "content": prompt}], "temperature": 0.3, "response_format": {"type": "json_object"}}, timeout=10)
        if response.status_code == 200: return json.loads(response.json()['choices'][0]['message']['content'])
        print(f"❌ Groq API Error: {response.status_code} - {response.text}")
        return None
    except Exception as e:
        print(f"❌ Groq AI Error: {e}")
        return None

CROP_INFO = {
    'rice': {'name': 'Rice', 'icon': '🌾', 'season': 'Kharif (June-Nov)', 'water': 'High (Standing Water)', 'soil': 'Clay/Clayey Loam', 'temp': '20-35°C'},
    'wheat': {'name': 'Wheat', 'icon': '🌾', 'season': 'Rabi (Nov-April)', 'water': 'Medium (4-6 Irrigations)', 'soil': 'Silty Loam', 'temp': '15-25°C'},
    'maize': {'name': 'Maize', 'icon': '🌽', 'season': 'Kharif/Rabi', 'water': 'Medium', 'soil': 'Well-drained Loam', 'temp': '22-30°C'},
    'cotton': {'name': 'Cotton', 'icon': '🌿', 'season': 'Kharif (May-Oct)', 'water': 'Medium', 'soil': 'Deep Black Soil', 'temp': '25-35°C'},
    'banana': {'name': 'Banana', 'icon': '🍌', 'season': 'Year-round', 'water': 'Very High', 'soil': 'Rich Volcanic/Alluvial', 'temp': '20-30°C'},
    'mango': {'name': 'Mango', 'icon': '🥭', 'season': 'Perennial', 'water': 'Low/Medium', 'soil': 'Deep Loamy', 'temp': '24-30°C'},
    'grapes': {'name': 'Grapes', 'icon': '🍇', 'season': 'Dec-May', 'water': 'Medium', 'soil': 'Sandy Loam', 'temp': '15-35°C'},
    'watermelon': {'name': 'Watermelon', 'icon': '🍉', 'season': 'Summer (Feb-June)', 'water': 'Medium', 'soil': 'Sandy to Sandy Loam', 'temp': '24-30°C'},
    'muskmelon': {'name': 'Muskmelon', 'icon': '🍈', 'season': 'Summer', 'water': 'Medium', 'soil': 'Sandy Loam', 'temp': '24-30°C'},
    'apple': {'name': 'Apple', 'icon': '🍎', 'season': 'Rabi (Oct-Feb)', 'water': 'Medium', 'soil': 'Well-drained Loam', 'temp': '10-25°C'},
    'orange': {'name': 'Orange', 'icon': '🍊', 'season': 'Year-round', 'water': 'Medium', 'soil': 'Light Loamy', 'temp': '13-37°C'},
    'papaya': {'name': 'Papaya', 'icon': '🥭', 'season': 'Year-round', 'water': 'Medium', 'soil': 'Well-drained Rich', 'temp': '25-30°C'},
    'coconut': {'name': 'Coconut', 'icon': '🥥', 'season': 'Perennial', 'water': 'High', 'soil': 'Sandy/Alluvial', 'temp': '20-30°C'},
    'pomegranate': {'name': 'Pomegranate', 'icon': '🍎', 'season': 'Year-round', 'water': 'Low', 'soil': 'Diverse (Well-drained)', 'temp': '25-35°C'},
    'coffee': {'name': 'Coffee', 'icon': '☕', 'season': 'Perennial', 'water': 'High', 'soil': 'Deep Rich Loam', 'temp': '15-28°C'},
    'tea': {'name': 'Tea', 'icon': '🍃', 'season': 'Perennial', 'water': 'High', 'soil': 'Acidic Forest Soil', 'temp': '13-32°C'},
    'tobacco': {'name': 'Tobacco', 'icon': '🍂', 'season': 'Rabi', 'water': 'Medium', 'soil': 'Sandy Loam', 'temp': '20-30°C'},
    'mungbean': {'name': 'Mungbean', 'icon': '🌱', 'season': 'Kharif/Summer', 'water': 'Low', 'soil': 'Loamy to Sandy Loam', 'temp': '25-35°C'},
    'blackgram': {'name': 'Blackgram', 'icon': '🌱', 'season': 'Kharif', 'water': 'Low', 'soil': 'Heavy Clay', 'temp': '25-35°C'},
    'lentil': {'name': 'Lentil', 'icon': '🍛', 'season': 'Rabi', 'water': 'Low', 'soil': 'Diverse Loams', 'temp': '18-30°C'},
    'pigeonpeas': {'name': 'Pigeonpeas', 'icon': '🌱', 'season': 'Kharif', 'water': 'Low', 'soil': 'Well-drained Loam', 'temp': '20-30°C'},
    'mothbeans': {'name': 'Mothbeans', 'icon': '🌱', 'season': 'Kharif/Summer', 'water': 'Very Low', 'soil': 'Sandy', 'temp': '25-35°C'},
    'chickpea': {'name': 'Chickpea', 'icon': '🥣', 'season': 'Rabi', 'water': 'Low', 'soil': 'Diverse Loams', 'temp': '15-25°C'},
    'kidneybeans': {'name': 'Kidney Beans', 'icon': '🧶', 'season': 'Rabi/Kharif', 'water': 'Medium', 'soil': 'Deep Silty Loam', 'temp': '15-25°C'},
    'jute': {'name': 'Jute', 'icon': '🧵', 'season': 'Kharif', 'water': 'High', 'soil': 'New Alluvial', 'temp': '24-34°C'},
}

MARKET_PRICES = [
    {'commodity': 'Basmati Rice', 'market': 'Azadpur', 'state': 'Delhi', 'min': 3500, 'max': 4500, 'modal': 4000, 'trend': 'up', 'change_percent': 5.2},
    {'commodity': 'Wheat', 'market': 'Khanna', 'state': 'Punjab', 'min': 2400, 'max': 2700, 'modal': 2550, 'trend': 'stable', 'change_percent': 0.1},
    {'commodity': 'Maize', 'market': 'Gultekdi', 'state': 'MS', 'min': 1800, 'max': 2100, 'modal': 1950, 'trend': 'down', 'change_percent': 2.5},
    {'commodity': 'Cotton', 'market': 'APMC Gujarat', 'state': 'GJ', 'min': 5800, 'max': 6400, 'modal': 6100, 'trend': 'up', 'change_percent': 3.8},
    {'commodity': 'Soybean', 'market': 'Indore', 'state': 'MP', 'min': 4200, 'max': 4800, 'modal': 4500, 'trend': 'up', 'change_percent': 1.5},
    {'commodity': 'Tomato', 'market': 'Kolar', 'state': 'KA', 'min': 600, 'max': 1200, 'modal': 900, 'trend': 'down', 'change_percent': 12.0},
]

@app.route('/')
def index(): return render_template('index.html')

@app.route('/api/ai-location')
def ai_location():
    lat, lon = request.args.get('lat', '28.6139'), request.args.get('lon', '77.2090')
    try:
        geo = requests.get(f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}", headers={'User-Agent': 'Agrinova'}, timeout=3).json()
        raw = geo.get('display_name', 'Unknown')
    except: raw = f"Lat:{lat}, Lon:{lon}"
    prompt = f"Analyze location for farming: {raw}. Provide farmer friendly address, agricultural zone, soil type, and major crops in JSON: {{address: '', zone: '', soil: '', crops: []}}"
    return jsonify(call_groq_ai(prompt) or {"address": raw, "zone": "Active Farm Land", "soil": "Alluvial", "crops": ["Wheat", "Rice"]})

@app.route('/api/weather')
def weather():
    lat, lon = request.args.get('lat', '28.6139'), request.args.get('lon', '77.2090')
    try:
        geo = requests.get(f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}", headers={'User-Agent': 'Agrinova'}, timeout=3).json()
        a = geo.get('address', {})
        city = a.get('city') or a.get('town') or a.get('village') or "Current Field"
    except: city = f"Section {lat[:4]}"
    
    t = random.randint(22, 36)
    h = random.randint(40, 85)
    return jsonify({
        'current': {'temperature': t, 'humidity': h, 'wind_speed': random.randint(5, 20), 'condition': 'Sunny' if h < 65 else 'Cloudy', 'icon': '☀️' if h < 65 else '☁️', 'location': city},
        'forecast': [{'day': 'Mon', 'max_temp': t+2, 'min_temp': t-4, 'condition': 'Sunny', 'icon': '☀️'}]
    })

@app.route('/api/analyze-weather')
def analyze_weather():
    lat, lon = request.args.get('lat', '28.6139'), request.args.get('lon', '77.2090')
    prompt = f"Analyze farming weather for {lat}, {lon}. Suggest current analysis, tips, and alerts. JSON: {{analysis: '', tips: [], alerts: []}}"
    return jsonify(call_groq_ai(prompt) or {"analysis": "Stable conditions.", "tips": ["Plant now"], "alerts": []})

@app.route('/api/farmer-news')
def farmer_news():
    news_items = ["Government increases MSP for Wheat.", "Heavy rain alert for Punjab.", "80% subsidy for drip irrigation.", "Fall Armyworm in Bihar Maize."]
    prompt = f"Analyze news: {news_items}. Categorize and summarize in JSON: {{top_stories: [{{title: '', impact: '', detail: '', category: ''}}], summary: ''}}"
    return jsonify(call_groq_ai(prompt) or {"top_stories": [{"title": "Market Update", "impact": "Positive", "detail": "Better returns.", "category": "Market"}], "summary": "Positive outlook."})

@app.route('/api/analyze-market')
def analyze_market():
    crop = request.args.get('crop', 'all')
    prompt = f"""Analyze real Mandi price trends for {crop} in India. 
    Provide a realistic 6-month sequence of modal prices (Jan to Jun) in ₹/quintal.
    JSON: {{
      "summary": "Short market trend summary",
      "grow_rec": "Yes/No",
      "income": "Profit estimate per acre",
      "reasoning": "Economic basis",
      "trend": [2100, 2250, 2180, 2400, 2600, 2750]
    }}"""
    return jsonify(call_groq_ai(prompt) or {
        "summary": "Stable trend.", "grow_rec": "Yes", "income": "Medium", 
        "reasoning": "Normal demand.", "trend": [1800, 2100, 1950, 2300, 2550, 2800]
    })

@app.route('/api/calculate-yield-ai', methods=['POST'])
def calculate_yield_ai():
    d = request.json
    prompt = f"Calculate yield, revenue, cost, profit for {d}. JSON: {{yield_qty: 0, revenue: 0, cost: 0, profit: 0, analysis: '', yield_boosters: [], cost_tips: []}}"
    return jsonify(call_groq_ai(prompt) or {"yield_qty": 100, "revenue": 200000, "cost": 50000, "profit": 150000, "analysis": "High potential.", "yield_boosters": ["NPK management"], "cost_tips": ["Solar pumps"]})

@app.route('/api/recommend-crop', methods=['POST'])
def recommend_crop():
    data = request.json or {}
    
    # Strict Realism-First Prompt
    prompt = f"""You are an elite agricultural decision support system. 
    REALISM is your priority. If factors mismatch, you must be honest.
    
    CRITICAL RULES:
    1. DO NOT give high confidence if ANY major factor mismatches: Soil, Climate, Water.
    2. If mismatch: Reduce confidence, mark as "Conditional", clearly explain why.
    3. PRIORITIZE: Soil compatibility > Climate > Water > Season.
    4. If soil is NOT suitable: Suggest better alternatives, do NOT rank as Best Match.
    5. Be realistic, not optimistic.
    
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
    
    # Icon matching
    crop_name = analysis.get('primary_recommendation', {}).get('crop', 'Wheat')
    info = CROP_INFO.get(crop_name.lower())
    if not info:
        for k, v in CROP_INFO.items():
            if k in crop_name.lower(): 
                info = v
                break
    analysis['primary_recommendation']['icon'] = info['icon'] if info else '🌱'
    
    return jsonify({"success": True, "data": analysis})

@app.route('/api/simplify-recommendation', methods=['POST'])
def simplify_recommendation():
    d = request.json
    prompt = f"Simplify this agricultural advice for a farmer in plain language. Original: {d}. JSON: {{simple_explanation: ''}}"
    return jsonify(call_groq_ai(prompt) or {"simple_explanation": "This crop is great for your soil. Plant it soon for best results."})

@app.route('/api/schemes')
def get_schemes():
    prompt = """Provide 4 Indian government schemes for farmers. JSON: {"schemes": [{"name": "", "icon": "", "description": "", "feature": "", "deadline": "", "apply_link": ""}]}"""
    data = call_groq_ai(prompt)
    if data and "schemes" in data: return jsonify(data["schemes"])
    return jsonify([{"name": "PM-KISAN", "icon": "💰", "description": "Income support.", "feature": "Direct Transfer", "deadline": "Ongoing", "apply_link": "https://pmkisan.gov.in"}])

@app.route('/api/mandi-prices')
def mandi_prices(): return jsonify(MARKET_PRICES)

@app.route('/api/soil-diagnosis', methods=['POST'])
def soil_diagnosis():
    data = request.json or {}
    stype = data.get('soil_type', 'Alluvial')
    ph = data.get('ph', 6.5)
    loc = data.get('location', 'India')
    
    prompt = f"""As a Soil Scientist, diagnose this soil and provide a logical basis for your findings.
    Type: {stype}, pH: {ph}, Location: {loc}
    Field Notes: {data.get('field_notes', 'None')}
    Current weather: {data.get('temperature', 25)}C, {data.get('rainfall', 100)}mm rainfall
    
    In the "diagnosis" field, explain the SCIENTIFIC BASIS of your estimation (e.g. "Based on the geological profile of {loc} and the {stype} soil type...").
    
    Return JSON:
    {{
      "health_score": "85%",
      "nutrient_status": {{
        "nitrogen": "Low/Medium/High",
        "phosphorus": "Low/Medium/High",
        "potassium": "Low/Medium/High"
      }},
      "composition": {{"sand": "40%", "silt": "30%", "clay": "30%"}},
      "diagnosis": "Summary of soil state",
      "treatment_plan": ["Action 1", "Action 2"],
      "biological_health": "Rating",
      "toxicity_risk": "Low/None"
    }}"""
    
    res = call_groq_ai(prompt) or {
        "health_score": "75%", 
        "nutrient_status": {"nitrogen": "Medium", "phosphorus": "Medium", "potassium": "Medium"},
        "composition": {"sand": "33%", "silt": "33%", "clay": "34%"},
        "diagnosis": "Initial assessment complete. Consider a lab test for precision.",
        "treatment_plan": ["Add organic compost"],
        "biological_health": "Fair", "toxicity_risk": "Low"
    }
    return jsonify({"success": True, "data": res})

@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    msg = request.json.get('message', '')
    prompt = f"Farming chatbot. User: {msg}. JSON: {{response: '...'}}"
    return jsonify(call_groq_ai(prompt) or {"response": "How can I help you?"})

if __name__ == '__main__': app.run(debug=True, port=5000)