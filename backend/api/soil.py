from flask import Blueprint, request, jsonify
from backend.utils.ai_helper import call_groq_ai

soil_bp = Blueprint('soil', __name__)

@soil_bp.route('/soil-diagnosis', methods=['POST'])
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
