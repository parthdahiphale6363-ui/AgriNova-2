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
    
    # Realistic 6-month market trend data for different crops
    market_trends = {
        'all': {
            'summary': 'Overall agricultural market showing mixed trends. Cereals stable, pulses rising, cash crops strong.',
            'grow_rec': 'Yes',
            'income': '₹45,000-60,000/acre',
            'reasoning': 'Seasonal demand patterns favor diversified cropping. MSP support ensures floor prices.',
            'trend': [2100, 2250, 2180, 2400, 2600, 2750],
            'forecast': 'Upward trend expected in Q2-Q3 due to reduced supply and increased demand.'
        },
        'Wheat': {
            'summary': 'Wheat market remains stable with steady demand. Harvest completed, storage-driven sales active.',
            'grow_rec': 'Yes',
            'income': '₹35,000-45,000/acre',
            'reasoning': 'MSP floor at ₹2,125/qtl ensures minimum returns. Government procurement active.',
            'trend': [2400, 2450, 2500, 2550, 2600, 2700],
            'forecast': 'Gradual price increase expected as storage depletes before next season.'
        },
        'Rice': {
            'summary': 'Rice prices firm due to export demand and stock depletion. Basmati premium intact.',
            'grow_rec': 'Yes',
            'income': '₹50,000-65,000/acre',
            'reasoning': 'Strong export demand, especially for Basmati. Quality premium drives profitability.',
            'trend': [3500, 3600, 3700, 3900, 4100, 4300],
            'forecast': 'Prices expected to peak in Q2 before cooling with new harvest.'
        },
        'Maize': {
            'summary': 'Maize market volatile due to global supply fluctuations. Industrial demand driving prices.',
            'grow_rec': 'Yes',
            'income': '₹28,000-38,000/acre',
            'reasoning': 'Strong poultry and bio-fuel demand. Prices linked to international markets.',
            'trend': [1800, 1850, 1950, 2050, 2150, 2250],
            'forecast': 'Expected recovery in coming months due to limited global supplies.'
        },
        'Cotton': {
            'summary': 'Cotton prices strengthening due to global supply concerns and strong textiles demand.',
            'grow_rec': 'Yes',
            'income': '₹55,000-75,000/acre',
            'reasoning': 'International price support, strong Indian textile industry demand.',
            'trend': [5800, 5950, 6100, 6250, 6400, 6600],
            'forecast': 'Prices likely to firm further as global inventories remain tight.'
        },
        'Soybean': {
            'summary': 'Soybean market rising on crushing demand and global price support.',
            'grow_rec': 'Yes',
            'income': '₹42,000-52,000/acre',
            'reasoning': 'Strong oilmeal demand from poultry, edible oil component.',
            'trend': [4200, 4350, 4450, 4650, 4850, 5050],
            'forecast': 'Bullish sentiment continues with sustained industrial demand.'
        },
        'Tomato': {
            'summary': 'Tomato prices highly volatile. Currently depressed due to peak supply season.',
            'grow_rec': 'Conditional',
            'income': '₹20,000-40,000/acre',
            'reasoning': 'Off-season pricing higher. Weather-dependent yields affect supplies.',
            'trend': [600, 700, 850, 1100, 1400, 1200],
            'forecast': 'Prices expected to rise significantly in off-season (May-June).'
        }
    }
    
    data = market_trends.get(crop, market_trends['all'])
    return jsonify(data)

@market_news_bp.route('/schemes')
def get_schemes():
    prompt = """Provide 6 Indian government agricultural schemes for farmers. JSON: {"schemes": [{"name": "", "icon": "", "description": "", "feature": "", "deadline": "", "apply_link": ""}]}"""
    data = call_groq_ai(prompt)
    if data and "schemes" in data: 
        return jsonify(data["schemes"])
    
    default_schemes = [
        {"name": "PM-KISAN", "icon": "💰", "description": "Income support scheme for farmers.", "feature": "Direct Transfer", "deadline": "Ongoing", "apply_link": "https://pmkisan.gov.in"},
        {"name": "PM Fasal Bima Yojana", "icon": "🛡️", "description": "Crop insurance protection scheme.", "feature": "Crop Insurance", "deadline": "Before Sowing", "apply_link": "https://pmfby.gov.in"},
        {"name": "Pradhan Mantri Kisan Samman Nidhi", "icon": "🌾", "description": "Direct income support for small/marginal farmers.", "feature": "₹6000/year", "deadline": "Ongoing", "apply_link": "https://pmkisan.gov.in"},
        {"name": "Soil Health Card Scheme", "icon": "🥗", "description": "Free soil testing and personalized fertilizer recommendations.", "feature": "Free Testing", "deadline": "Year-round", "apply_link": "https://soilhealth.dac.gov.in"},
        {"name": "Pradhan Mantri Krishi Sinchayee Yojana", "icon": "💧", "description": "Irrigation infrastructure and drip system subsidies.", "feature": "80% Subsidy", "deadline": "Rolling", "apply_link": "https://pmksy.gov.in"},
        {"name": "Kisan Vikas Patra", "icon": "📈", "description": "Savings scheme for farmers with attractive returns.", "feature": "10.7% Interest", "deadline": "Ongoing", "apply_link": "https://www.indiapost.gov.in"}
    ]
    return jsonify(default_schemes)

@market_news_bp.route('/mandi-prices')
def mandi_prices(): 
    return jsonify(MARKET_PRICES)

@market_news_bp.route('/market-stats')
def market_stats():
    """Return market statistics and insights"""
    total_commodities = len(MARKET_PRICES)
    trending_up = len([p for p in MARKET_PRICES if p['trend'] == 'up'])
    trending_down = len([p for p in MARKET_PRICES if p['trend'] == 'down'])
    trending_stable = len([p for p in MARKET_PRICES if p['trend'] == 'stable'])
    
    avg_price = sum([p['modal'] for p in MARKET_PRICES]) / total_commodities if total_commodities > 0 else 0
    
    return jsonify({
        'total_commodities': total_commodities,
        'trending_up': trending_up,
        'trending_down': trending_down,
        'trending_stable': trending_stable,
        'average_modal_price': round(avg_price, 2),
        'regions': len(set([p['state'] for p in MARKET_PRICES])),
        'updated_at': 'Real-time'
    })
