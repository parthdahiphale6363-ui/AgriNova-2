from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Agrinova is working!',
        'created_by': 'Parth Dahiphale',
        'venv': 'Active'
    })

if __name__ == '__main__':
    print("🚀 Starting Agrinova test server...")
    print("📍 Open http://localhost:5000 in your browser")
    app.run(debug=True, port=5000)