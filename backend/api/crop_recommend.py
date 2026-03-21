"""
Agrinova - Crop Recommendation API
Created by Parth Dahiphale
"""

from flask import Blueprint, request, jsonify, current_app
import joblib
import numpy as np
import pandas as pd
from datetime import datetime
import logging

crop_bp = Blueprint('crop', __name__)
logger = logging.getLogger(__name__)

# Load models (will be loaded from app context)
ensemble_model = None
label_encoder = None
scaler = None

def load_models():
    """Load AI models"""
    global ensemble_model, label_encoder, scaler
    try:
        ensemble_model = joblib.load('backend/models/saved_models/ensemble_model.pkl')
        label_encoder = joblib.load('backend/models/saved_models/label_encoder.pkl')
        scaler = joblib.load('backend/models/saved_models/scaler.pkl')
        logger.info("✅ Crop recommendation models loaded")
    except Exception as e:
        logger.error(f"❌ Failed to load models: {e}")

# Crop database with detailed information
CROP_DATABASE = {
    'rice': {
        'name': 'Rice',
        'scientific_name': 'Oryza sativa',
        'season': 'Kharif (June-October)',
        'water_requirement': 'High (1200-1500 mm)',
        'soil_type': 'Clay loam, alluvial',
        'temperature_range': '20-35°C',
        'fertilizer_npk': '120:60:40 kg/ha',
        'duration': '120-150 days',
        'yield_per_hectare': '4-5 tons',
        'profit_per_hectare': '₹45,000-60,000',
        'states': ['West Bengal', 'Uttar Pradesh', 'Punjab', 'Tamil Nadu', 'Andhra Pradesh'],
        'tips': [
            'Use high-yielding varieties like Pusa 44 or PR 126',
            'Maintain 2-3 cm water depth during vegetative stage',
            'Apply zinc sulfate at 25 kg/ha for better yield'
        ]
    },
    'wheat': {
        'name': 'Wheat',
        'scientific_name': 'Triticum aestivum',
        'season': 'Rabi (November-April)',
        'water_requirement': 'Medium (450-650 mm)',
        'soil_type': 'Loamy, clay loam',
        'temperature_range': '15-25°C',
        'fertilizer_npk': '120:60:40 kg/ha',
        'duration': '110-130 days',
        'yield_per_hectare': '4.5-5.5 tons',
        'profit_per_hectare': '₹50,000-65,000',
        'states': ['Uttar Pradesh', 'Punjab', 'Haryana', 'Madhya Pradesh', 'Rajasthan'],
        'tips': [
            'Plant HD 2967 or PBW 723 varieties for high yield',
            'Ensure proper drainage in fields',
            'Apply first irrigation 21-25 days after sowing'
        ]
    },
    'maize': {
        'name': 'Maize',
        'scientific_name': 'Zea mays',
        'season': 'All seasons',
        'water_requirement': 'Medium (500-800 mm)',
        'soil_type': 'Well-drained loamy',
        'temperature_range': '22-30°C',
        'fertilizer_npk': '150:75:60 kg/ha',
        'duration': '90-110 days',
        'yield_per_hectare': '5-6 tons',
        'profit_per_hectare': '₹40,000-55,000',
        'states': ['Karnataka', 'Madhya Pradesh', 'Bihar', 'Telangana', 'Maharashtra'],
        'tips': [
            'Plant hybrid varieties like NK 6240 or Pioneer 3377',
            'Maintain plant population of 60,000-65,000 per hectare',
            'Harvest when husk turns brown and grains are hard'
        ]
    },
    'cotton': {
        'name': 'Cotton',
        'scientific_name': 'Gossypium spp.',
        'season': 'Kharif (May-September)',
        'water_requirement': 'Medium (700-1000 mm)',
        'soil_type': 'Black cotton soil, alluvial',
        'temperature_range': '25-35°C',
        'fertilizer_npk': '120:60:60 kg/ha',
        'duration': '150-180 days',
        'yield_per_hectare': '4-5 bales',
        'profit_per_hectare': '₹60,000-80,000',
        'states': ['Gujarat', 'Maharashtra', 'Telangana', 'Andhra Pradesh', 'Punjab'],
        'tips': [
            'Use Bt cotton hybrids for pest resistance',
            'Maintain spacing of 90x60 cm for optimal growth',
            'Monitor for bollworms regularly'
        ]
    },
    'sugarcane': {
        'name': 'Sugarcane',
        'scientific_name': 'Saccharum officinarum',
        'season': 'All seasons',
        'water_requirement': 'High (1500-2500 mm)',
        'soil_type': 'Deep loamy, alluvial',
        'temperature_range': '20-35°C',
        'fertilizer_npk': '250:90:120 kg/ha',
        'duration': '10-12 months',
        'yield_per_hectare': '70-80 tons',
        'profit_per_hectare': '₹1,20,000-1,50,000',
        'states': ['Uttar Pradesh', 'Maharashtra', 'Karnataka', 'Tamil Nadu', 'Bihar'],
        'tips': [
            'Plant CO 86032 or CO 0238 varieties',
            'Ensure adequate moisture throughout growth',
            'Remove dry leaves periodically'
        ]
    },
    'groundnut': {
        'name': 'Groundnut',
        'scientific_name': 'Arachis hypogaea',
        'season': 'Kharif & Rabi',
        'water_requirement': 'Low (350-500 mm)',
        'soil_type': 'Sandy loam, well-drained',
        'temperature_range': '24-30°C',
        'fertilizer_npk': '20:60:40 kg/ha',
        'duration': '120-150 days',
        'yield_per_hectare': '2-2.5 tons',
        'profit_per_hectare': '₹35,000-45,000',
        'states': ['Gujarat', 'Andhra Pradesh', 'Tamil Nadu', 'Karnataka', 'Maharashtra'],
        'tips': [
            'Use TMV 2 or Kadiri 6 varieties',
            'Apply gypsum at 500 kg/ha at flowering',
            'Harvest when leaves turn yellow'
        ]
    }
}

@crop_bp.route('/recommend', methods=['POST'])
def recommend_crop():
    """
    Get AI-powered crop recommendation based on soil and climate conditions
    """
    try:
        # Get input data
        data = request.json
        
        # Validate required fields
        required_fields = ['nitrogen', 'phosphorus', 'potassium', 'temperature', 
                          'humidity', 'ph', 'rainfall']
        
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Extract features
        features = [
            float(data['nitrogen']),
            float(data['phosphorus']),
            float(data['potassium']),
            float(data['temperature']),
            float(data['humidity']),
            float(data['ph']),
            float(data['rainfall'])
        ]
        
        # Get user info (optional)
        user_id = data.get('user_id')
        
        # Load models if not loaded
        if ensemble_model is None:
            load_models()
        
        # Scale features
        features_scaled = scaler.transform([features])
        
        # Get ensemble prediction
        prediction_encoded = ensemble_model.predict(features_scaled)[0]
        probabilities = ensemble_model.predict_proba(features_scaled)[0]
        
        # Get crop name
        crop = label_encoder.inverse_transform([prediction_encoded])[0]
        confidence = float(probabilities[prediction_encoded])
        
        # Get top 5 recommendations
        top_5_indices = np.argsort(probabilities)[-5:][::-1]
        top_5_crops = label_encoder.inverse_transform(top_5_indices)
        top_5_probs = probabilities[top_5_indices]
        
        recommendations = []
        for i in range(5):
            crop_name = top_5_crops[i].lower()
            recommendations.append({
                'rank': i + 1,
                'crop': top_5_crops[i],
                'confidence': float(top_5_probs[i]),
                'details': CROP_DATABASE.get(crop_name, {
                    'name': top_5_crops[i],
                    'season': 'Contact local agricultural officer',
                    'water_requirement': 'Varies by region',
                    'soil_type': 'Contact local agricultural officer',
                    'temperature_range': 'Varies by region'
                })
            })
        
        # Get detailed information for primary recommendation
        primary_crop_info = CROP_DATABASE.get(crop.lower(), {
            'name': crop,
            'season': 'Contact local agricultural officer',
            'water_requirement': 'Varies by region',
            'soil_type': 'Contact local agricultural officer',
            'temperature_range': 'Varies by region',
            'fertilizer_npk': 'Contact local agricultural officer',
            'duration': 'Varies by variety',
            'yield_per_hectare': 'Contact local agricultural officer',
            'profit_per_hectare': 'Contact local agricultural officer',
            'states': ['All regions'],
            'tips': [
                'Consult local agricultural extension officer',
                'Test soil before planting',
                'Use quality seeds from certified sources'
            ]
        })
        
        response = {
            'success': True,
            'timestamp': datetime.now().isoformat(),
            'primary_recommendation': {
                'crop': crop,
                'confidence': confidence,
                'details': primary_crop_info
            },
            'top_5_recommendations': recommendations,
            'input_parameters': {
                'nitrogen': features[0],
                'phosphorus': features[1],
                'potassium': features[2],
                'temperature': features[3],
                'humidity': features[4],
                'ph': features[5],
                'rainfall': features[6]
            },
            'message': f"Based on your soil and climate conditions, {crop} is the most suitable crop with {confidence*100:.1f}% confidence."
        }
        
        # Save to database if user_id provided
        if user_id:
            try:
                from app import CropHistory, db
                history = CropHistory(
                    user_id=user_id,
                    soil_n=features[0],
                    soil_p=features[1],
                    soil_k=features[2],
                    temperature=features[3],
                    humidity=features[4],
                    ph=features[5],
                    rainfall=features[6],
                    recommended_crop=crop,
                    confidence=confidence
                )
                db.session.add(history)
                db.session.commit()
            except Exception as e:
                logger.error(f"Failed to save history: {e}")
        
        return jsonify(response), 200
        
    except Exception as e:
        logger.error(f"Error in crop recommendation: {str(e)}")
        return jsonify({'error': str(e)}), 500

@crop_bp.route('/crops', methods=['GET'])
def get_all_crops():
    """Get list of all supported crops"""
    return jsonify({
        'crops': list(CROP_DATABASE.keys()),
        'count': len(CROP_DATABASE)
    })

@crop_bp.route('/crop/<crop_name>', methods=['GET'])
def get_crop_details(crop_name):
    """Get detailed information about a specific crop"""
    crop_info = CROP_DATABASE.get(crop_name.lower())
    if crop_info:
        return jsonify(crop_info)
    return jsonify({'error': 'Crop not found'}), 404

@crop_bp.route('/history/<int:user_id>', methods=['GET'])
def get_user_history(user_id):
    """Get crop recommendation history for a user"""
    try:
        from app import CropHistory
        history = CropHistory.query.filter_by(user_id=user_id)\
                   .order_by(CropHistory.created_at.desc())\
                   .limit(10).all()
        
        result = []
        for h in history:
            result.append({
                'date': h.created_at.isoformat(),
                'nitrogen': h.soil_n,
                'phosphorus': h.soil_p,
                'potassium': h.soil_k,
                'temperature': h.temperature,
                'humidity': h.humidity,
                'ph': h.ph,
                'rainfall': h.rainfall,
                'recommended_crop': h.recommended_crop,
                'confidence': h.confidence
            })
        
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500