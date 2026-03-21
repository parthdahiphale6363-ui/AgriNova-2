from flask import Flask, render_template
from flask_cors import CORS
from backend.config import Config

def create_app():
    app = Flask(__name__, 
                static_folder='../frontend', 
                template_folder='../frontend', 
                static_url_path='')
    
    app.config.from_object(Config)
    CORS(app)

    # Import and register blueprints
    from backend.api.farming import farming_bp
    from backend.api.weather import weather_bp
    from backend.api.market_news import market_news_bp
    from backend.api.soil import soil_bp
    from backend.api.chatbot import chatbot_bp

    app.register_blueprint(farming_bp, url_prefix='/api')
    app.register_blueprint(weather_bp, url_prefix='/api')
    app.register_blueprint(market_news_bp, url_prefix='/api')
    app.register_blueprint(soil_bp, url_prefix='/api')
    app.register_blueprint(chatbot_bp, url_prefix='/api')

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
