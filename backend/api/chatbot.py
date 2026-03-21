from flask import Blueprint, request, jsonify
from backend.utils.ai_helper import call_groq_ai

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/chatbot', methods=['POST'])
def chatbot():
    msg = request.json.get('message', '')
    prompt = f"Farming chatbot. User: {msg}. JSON: {{response: '...'}}"
    return jsonify(call_groq_ai(prompt) or {"response": "How can I help you?"})
