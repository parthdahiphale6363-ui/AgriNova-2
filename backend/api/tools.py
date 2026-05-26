from flask import Blueprint, request, jsonify
from backend.utils.ai_helper import call_groq_ai

tools_bp = Blueprint('tools_bp', __name__)

@tools_bp.route('/diagnose-disease', methods=['POST'])
def diagnose_disease():
    data = request.json or {}
    crop = data.get('crop', 'unknown crop')
    symptoms = data.get('symptoms', '')
    
    if not symptoms:
        return jsonify({"success": False, "error": "Symptoms are required for diagnosis"})

    prompt = f"""
    You are an expert plant pathologist. A farmer reports the following symptoms on their {crop} crop:
    "{symptoms}"
    
    Diagnose the most likely disease or pest issue based on these symptoms.
    Respond ONLY with a valid JSON object matching this schema exactly:
    {{
      "disease_name": "Name of the disease or pest",
      "severity": "Low" | "Medium" | "High",
      "treatment_plan": ["step 1", "step 2", "step 3"],
      "preventive_measures": ["measure 1", "measure 2"]
    }}
    """
    
    ai_response = call_groq_ai(prompt)
    if not ai_response:
        # Fallback
        ai_response = {
            "disease_name": f"Possible issue with {crop}",
            "severity": "Medium",
            "treatment_plan": ["Consult a local agricultural expert", "Apply standard fungicide/pesticide carefully"],
            "preventive_measures": ["Improve drainage and air circulation", "Monitor crops daily"]
        }
        
    return jsonify({
        "success": True,
        "data": ai_response
    })

@tools_bp.route('/fertilizer-dose', methods=['POST'])
def fertilizer_dose():
    data = request.json or {}
    crop = data.get('crop', 'wheat')
    area_acres = data.get('area_acres', 1)
    n_status = data.get('nitrogen_status', 'Medium')
    p_status = data.get('phosphorus_status', 'Medium')
    k_status = data.get('potassium_status', 'Medium')
    growth_stage = data.get('growth_stage', 'Vegetative')

    prompt = f"""
    You are an expert agronomist. Calculate the exact fertilizer requirements for:
    Crop: {crop}
    Area: {area_acres} acres
    Soil Nitrogen Status: {n_status}
    Soil Phosphorus Status: {p_status}
    Soil Potassium Status: {k_status}
    Current Growth Stage: {growth_stage}
    
    Provide the exact fertilizer dose recommendations in kg per acre.
    Respond ONLY with a valid JSON object matching this schema exactly:
    {{
      "nitrogen_kg_per_acre": 50,
      "phosphorus_kg_per_acre": 20,
      "potassium_kg_per_acre": 30,
      "application_timing": "Describe exactly when and how to apply these fertilizers",
      "organic_alternatives": ["Alternative 1", "Alternative 2"]
    }}
    """
    
    ai_response = call_groq_ai(prompt)
    if not ai_response:
        ai_response = {
            "nitrogen_kg_per_acre": 40,
            "phosphorus_kg_per_acre": 20,
            "potassium_kg_per_acre": 20,
            "application_timing": "Apply in splits: half at sowing, half during vegetative stage.",
            "organic_alternatives": ["Farmyard Manure (FYM)", "Vermicompost", "Neem Cake"]
        }
        
    return jsonify({
        "success": True,
        "data": ai_response
    })

@tools_bp.route('/crop-rotation', methods=['POST'])
def crop_rotation():
    data = request.json or {}
    prev_crop = data.get('previous_crop', 'unknown')
    soil_type = data.get('soil_type', 'unknown')
    location = data.get('location', 'India')
    season = data.get('season', 'Kharif')

    prompt = f"""
    You are an expert crop rotation planner. Recommend the best next crops based on:
    Previous Crop Grown: {prev_crop}
    Soil Type: {soil_type}
    Location: {location}
    Upcoming Season: {season}
    
    Provide the top 3 best crop suggestions to plant next to replenish the soil and maximize profits.
    Respond ONLY with a valid JSON object matching this schema exactly:
    {{
      "recommendations": [
        {{
          "crop": "Crop Name",
          "reason": "Why this crop is good for soil replenishment, profit, and water needs"
        }},
        {{
          "crop": "Crop Name 2",
          "reason": "..."
        }},
        {{
          "crop": "Crop Name 3",
          "reason": "..."
        }}
      ]
    }}
    """
    
    ai_response = call_groq_ai(prompt)
    if not ai_response or "recommendations" not in ai_response:
        ai_response = {
            "recommendations": [
                {"crop": "Legumes/Pulses", "reason": "Fixes nitrogen in the soil, excellent after heavy feeders."},
                {"crop": "Green Manure (Dhaincha)", "reason": "Improves soil organic matter and structure."},
                {"crop": "Maize", "reason": "Good break crop with decent market value."}
            ]
        }
        
    return jsonify({
        "success": True,
        "data": ai_response
    })
