from flask import Blueprint, request, jsonify
import requests
import random
from backend.utils.ai_helper import call_groq_ai

weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/weather')
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

@weather_bp.route('/analyze-weather')
def analyze_weather():
    lat, lon = request.args.get('lat', '28.6139'), request.args.get('lon', '77.2090')
    prompt = f"Analyze farming weather for {lat}, {lon}. Suggest current analysis, tips, and alerts. JSON: {{analysis: '', tips: [], alerts: []}}"
    return jsonify(call_groq_ai(prompt) or {"analysis": "Stable conditions.", "tips": ["Plant now"], "alerts": []})
