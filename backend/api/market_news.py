from flask import Blueprint, request, jsonify
from backend.utils.ai_helper import call_groq_ai
from backend.utils.constants import MARKET_PRICES

market_news_bp = Blueprint('market_news', __name__)

@market_news_bp.route('/farmer-news')
def farmer_news():
    news_items = ["Government increases MSP for Wheat.", "Heavy rain alert for Punjab.", "80% subsidy for drip irrigation.", "Fall Armyworm in Bihar Maize."]
    prompt = f"Analyze news: {news_items}. Categorize and summarize in JSON: {{top_stories: [{{title: '', impact: '', detail: '', category: ''}}], summary: ''}}"
    return jsonify(call_groq_ai(prompt) or {"top_stories": [{"title": "Market Update", "impact": "Positive", "detail": "Better returns.", "category": "Market"}], "summary": "Positive outlook."})

@market_news_bp.route('/analyze-market')
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

@market_news_bp.route('/schemes')
def get_schemes():
    prompt = """Provide 4 Indian government schemes for farmers. JSON: {"schemes": [{"name": "", "icon": "", "description": "", "feature": "", "deadline": "", "apply_link": ""}]}"""
    data = call_groq_ai(prompt)
    if data and "schemes" in data: return jsonify(data["schemes"])
    return jsonify([{"name": "PM-KISAN", "icon": "💰", "description": "Income support.", "feature": "Direct Transfer", "deadline": "Ongoing", "apply_link": "https://pmkisan.gov.in"}])

@market_news_bp.route('/mandi-prices')
def mandi_prices(): 
    return jsonify(MARKET_PRICES)
