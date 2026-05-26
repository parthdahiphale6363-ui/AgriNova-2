# 🌾 AGRINOVA — AI-Powered Farming Assistant

[![Python Version](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)
[![Flask Version](https://img.shields.io/badge/flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![Groq AI](https://img.shields.io/badge/groq-LLaMA%203.3%2070B-blueviolet.svg)](https://console.groq.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![PWA](https://img.shields.io/badge/PWA-enabled-success.svg)](manifest.json)

**Created by Parth Dahiphale** | 2026

AGRINOVA is a state-of-the-art, interactive, and intelligent AI-powered farming assistant. Designed specifically to empower Indian farmers, the platform provides real-time, location-based agricultural insights, smart crop recommendations, scientific soil diagnosis, climate forecasting, mandi market prices, pest risk advisories, and direct links to government welfare schemes.

---

## 📋 Table of Contents
1. [Overview & Core Value Propositions](#-overview--core-value-propositions)
2. [Key Features](#-key-features)
3. [Tech Stack](#-tech-stack)
4. [Project Structure & Placeholder Registry](#-project-structure--placeholder-registry)
5. [How It Works](#-how-it-works)
6. [Offline & PWA Capabilities](#-offline--pwa-capabilities)
7. [Comprehensive API Reference](#-comprehensive-api-reference)
8. [Installation & Setup](#-installation--setup)
9. [Deployment & Infrastructure Configurations](#-deployment--infrastructure-configurations)
10. [Usage Guide](#-usage-guide)
11. [Supported Crops](#-supported-crops)
12. [Developer Reference](#-developer-reference)
13. [Future Roadmap](#-future-roadmap)
14. [Contributing & License](#-contributing--license)

---

## 🌾 Overview & Core Value Propositions

AGRINOVA is a comprehensive agricultural decision-support platform that acts as a 24/7 personal digital agronomist. By linking localized sensor/weather telemetry with advanced LLM intelligence (LLaMA 3.3 70B via Groq Cloud), AGRINOVA translates complex scientific data into plain, actionable advice.

### Core Strengths
*   **Contextual Realism**: If critical parameters (like soil type, pH, or local climate) are incompatible with the desired crop, the system outputs an honest "Conditional" rank with reduced confidence scores and details alternate suggestions.
*   **PWA-First Architecture**: Built with a service worker (`sw.js`) that caches static files, records successful API responses, and serves a dedicated, auto-reloading offline dashboard if internet connection is lost.
*   **Zero-Config Location Telemetry**: Auto-detects coordinate geolocations via HTML5 Geolocation API, query Open-Meteo for hyper-local forecasts, and performs reverse-geocoding via Nominatim (OpenStreetMap) to customize AI prompts.
*   **Comprehensive Financial Analysis**: Helps farmers project yields, revenues, and operating costs, generating specific cost-saving tips and yield-boosting advice.

---

## 🚀 Key Features

### 1. AI-Powered Crop Recommendation
*   Analyzes **10 key parameters**: Soil type, pH level, temperature, humidity, rainfall, water source, district/state, sowing month, and custom field notes.
*   Generates a weighted confidence level (`X%`), compatibility score card (Soil, Climate, Water), and risk assessment level (Low/Medium/High).
*   Recommends alternative crops, fertilizer schedules (N-P-K ratios), irrigation strategies, and pesticide directions.

### 2. Scientific Soil Diagnosis
*   Computes an **AI Soil Health Score** (0-100%).
*   Estimates physical soil composition (visualized in a Sand/Silt/Clay percentage bar).
*   Estimates NPK Nutrient levels (Low/Medium/High) and generates an **AI Treatment Plan** outlining compost additions, pH neutralization, and drainage methods.

### 3. Yield & Profit Calculator
*   Accepts crop type, cultivated acreage, irrigation method, soil type, and target market price per quintal.
*   Uses Groq AI to calculate projected yield volume, gross revenue, total cost (seeds, labor, fertilizer, water), and net profit/loss.
*   Suggests cost-saving recommendations and tailored yield-booster strategies.

### 4. Interactive Crop Calendar
*   A visual schedule mapping month-by-month cycles for major crops.
*   Highlights optimal windows for **Sowing**, **Growth**, and **Harvesting** with a "Current Month Indicator".
*   Supports wheat, rice, maize, cotton, sugarcane, and soybean.

### 5. Pest & Disease Alert Center
*   Monitors risk levels (Low/Medium/High) for prevalent pests and blights:
    *   **Aphids** (Wheat, Mustard)
    *   **Brown Plant Hopper** (Rice/Paddy)
    *   **Whitefly** (Cotton, Tomato)
    *   **Leaf Blight** (Maize, Sorghum)
    *   **Stem Borer** (Sugarcane)
    *   **Powdery Mildew** (Grapes, Vegetables)
*   Provides actionable control tips (biological control, chemical sprays, trap setups) for each.

### 6. Live Mandi Market Prices
*   Retrieves live commodity prices across Indian markets (e.g., Basmati Rice, Wheat, Maize, Cotton, Soybean, Tomato) containing minimum, maximum, and modal values.
*   Calculates price trends (Up 📈, Down 📉, Stable ➡️) and change percentages.
*   Includes interactive search filtering and a **6-Month Price Trend Chart** (Chart.js line graph) powered by Groq market sentiment analysis.

### 7. Government Schemes & Welfare Portal
*   Fetches active agricultural schemes and subsidies (e.g., PM-KISAN, Drip Irrigation Subsidies, PM Fasal Bima Yojana).
*   Specifies detailed benefits, eligibility criteria, application status, and direct external application links.

### 8. Live News & Alerts Ticker
*   Auto-fetches and summarizes major agricultural news, policy changes, MSP adjustments, and weather warnings.
*   Features a rolling alerts ticker in the dashboard header.

### 9. AI Chatbot Assistant (Groq)
*   Collapsible chatbot interface available on every page.
*   Answers farming questions, interprets weather patterns, translates terms, and guides fertilizer applications.
*   Supports quick-reply prompt chips for common inquiries.

---

## 🛠️ Tech Stack

### Backend
*   **Flask 2.3.3**: Lightweight web server and JSON REST API gateway.
*   **Flask-CORS 4.0.0**: Enables Cross-Origin Resource Sharing during development.
*   **python-dotenv**: Loads configuration and environment keys from a secure `.env` file.
*   **requests 2.31.0**: Handles downstream API calls to OpenStreetMap and Groq.
*   **gunicorn 21.2.0**: WSGI HTTP Server for production deployments.

### Frontend
*   **HTML5 & CSS3**: Responsive, semantic layout with rich glassmorphic cards and micro-animations.
*   **Vanilla JavaScript (ES6+)**: Handles asynchronous network fetching, client geolocation, and UI rendering.
*   **Chart.js**: Render dynamic mandi price history line charts with customized tooltips.
*   **AOS (Animate On Scroll) & Animate.css**: Delivers premium transition effects.
*   **Font Awesome 6.0.0**: Used for consistent, recognizable iconography.

### AI & API Integrations
*   **Groq Cloud API**: Serves LLaMA-3.3-70B-versatile model responses with a strict `json_object` schema constraint to ensure API payloads are always parseable.
*   **Open-Meteo API**: Fetches latitude/longitude coordinate weather telemetry without requiring keys.
*   **Nominatim API (OpenStreetMap)**: Decodes geographic coordinates into human-readable locations.

---

## 📁 Project Structure & Placeholder Registry

The project directory layout separates backend modules, frontend assets, configurations, and deployment definitions. 

> [!NOTE]
> Several files in the workspace function as placeholders (zero-byte files) to support future database and modular JS migrations. For maximum performance and simplicity, their active implementation is currently handled inline inside [index.html](file:///c:/Users/Asus/Desktop/AGRINOVA-main/frontend/index.html) and direct backend controller files.

```
AGRINOVA/
│
├── 📄 app.py                      # Flask application entry point
├── 📄 requirements.txt            # Main Python dependency manifest
├── 📄 runtime.txt                 # Specifies Python version for cloud build engines
├── 📄 Procfile                    # Heroku dyno deployment configuration
├── 📄 railway.json                # Railway.app configuration file
├── 📄 vercel.json                 # Vercel deployment configuration
├── 📄 LICENSE                     # MIT License
├── 📄 README.md                   # This documentation file
│
├── 📁 backend/                    # Core Python Application
│   ├── 📄 __init__.py            # Flask Application Factory (Blueprint initialization)
│   ├── 📄 config.py              # Environment configuration & API URL registry
│   ├── 📄 requirements.txt        # Backend specific dependencies
│   │
│   ├── 📁 api/                   # REST API Blueprint Endpoints
│   │   ├── 📄 chatbot.py         # Handles '/api/chatbot' interactions
│   │   ├── 📄 farming.py         # Coordinates crop recommendations, yield and location logic
│   │   ├── 📄 market_news.py     # Delivers Mandi prices, active news, and government schemes
│   │   ├── 📄 soil.py            # Generates scientific soil health metrics
│   │   └── 📄 weather.py         # Manages climate telemetry & forecasts
│   │
│   ├── 📁 database/              # Database Configuration (Placeholders)
│   │   ├── 📄 __init__.py        # Empty module init
│   │   ├── 📄 db_config.py       # [Placeholder] Intended for DB connection pools
│   │   └── 📄 models.py          # [Placeholder] Intended for SQL Alchemy ORM definitions
│   │
│   ├── 📁 models/                # Machine Learning Models (Placeholders)
│   │   ├── 📄 crop_model.py      # [Placeholder] Intended for offline TensorFlow/Sklearn models
│   │   └── 📁 saved_models/      # [Placeholder] Pre-trained serialization binaries (.pkl)
│   │
│   └── 📁 utils/                 # Auxiliary Helpers
│       ├── 📄 ai_helper.py       # Groq API connection wrapper (JSON Schema enforcement)
│       ├── 📄 constants.py       # Hardcoded crop attributes and Mandi rate lists
│       ├── 📄 data_fetcher.py    # [Placeholder] Intended for third-party caching tasks
│       └── 📄 validators.py      # [Placeholder] Intended for JSON validation filters
│
├── 📁 frontend/                   # Client-Side Assets
│   ├── 📄 index.html             # Main Frontend SPA (combines Dashboard, Calculator, Forms, JS)
│   ├── 📄 sw.js                  # Service worker managing caching & offline functionality
│   │
│   ├── 📁 pages/                 # Secondary Pages (Placeholders - active logic is in index.html)
│   │   ├── 📄 about.html         # [Placeholder]
│   │   ├── 📄 contact.html       # [Placeholder]
│   │   └── 📄 dashboard.html     # [Placeholder]
│   │
│   ├── 📁 css/                   # Stylesheets
│   │   ├── 📄 style.css          # Main styling framework (glassmorphic layout, theme colors)
│   │   ├── 📄 responsive.css     # Mobile viewport layout & grid adjustments
│   │   └── 📄 animations.css     # Keyframe transformations & spinner classes
│   │
│   └── 📁 js/                    # Modular JS Files (Placeholders - active logic is in index.html)
│       ├── 📄 main.js            # General UI controls (theme toggle, language selector, preloader)
│       ├── 📄 chatbot.js         # [Placeholder]
│       ├── 📄 crop.js            # [Placeholder]
│       ├── 📄 prices.js          # [Placeholder]
│       ├── 📄 schemes.js         # [Placeholder]
│       └── 📄 weather.js         # [Placeholder]
│
├── 📁 data/                       # Local Storage
│   ├── 📁 raw/                   # [Placeholder] Raw CSV/JSON datasets
│   └── 📁 processed/             # [Placeholder] Normalized ML datasets
│
└── 📁 instance/                   # Local Instance cache space (SQLite db target)
```

---

## 🔄 How It Works

```
                        +----------------------------+
                        |  Farmer Opens AGRINOVA App |
                        +----------------------------+
                                      |
                                      v
                        +----------------------------+
                        | Coordinates Geolocation    |
                        | Auto-Detected by Browser   |
                        +----------------------------+
                                      |
              +-----------------------+-----------------------+
              |                                               |
              v                                               v
  +-----------------------+                       +-----------------------+
  |  Hits Nominatim API   |                       |  Hits Open-Meteo API  |
  |  (Reverse Geocoding)  |                       |  (Coordinates Weather)|
  +-----------------------+                       +-----------------------+
              |                                               |
              | Human-Readable Address                        | Live Forecast Telemetry
              +-----------------------+-----------------------+
                                      |
                                      v
                        +----------------------------+
                        |   Formulates Prompt &      |
                        |   Queries Backend APIs     |
                        +----------------------------+
                                      |
                                      v
                        +----------------------------+
                        | Groq Cloud (LLaMA 3.3)     |
                        | Enforces Strict JSON Output|
                        +----------------------------+
                                      |
                                      v
                        +----------------------------+
                        |  Renders Interactive UI:   |
                        |  - Compatibility Scores    |
                        |  - Soil NPK Treatment      |
                        |  - Financial Yield Chart   |
                        +----------------------------+
```

---

## 📱 Offline & PWA Capabilities

AGRINOVA is built to remain useful in rural fields where network connectivity can be highly unstable:

### ⚙️ Service Worker Caching Rules (`sw.js`)
*   **Static Assets**: On installation, the service worker pre-caches core layout sheets (`style.css`, `responsive.css`, `animations.css`, `main.js`) and structural assets.
*   **Dynamic API Interceptor**: For any backend API routes (matching `/api/`), the service worker attempts to pull a fresh response from the network. If the network call fails, it automatically falls back to the **last successful cached response** matching that specific request signature.
*   **PWA Manifest shortcuts**: The `manifest.json` file configures shortcuts enabling users to jump straight into "Crop Recommendation", "Market Prices", or "Weather" sections from their device homescreen.

### 🔌 Seamless Offline Fallback Dashboard
If a user is completely offline during navigation, the service worker intercepts the request and injects a dedicated Offline Fallback Page featuring:
*   An agricultural theme styled inline.
*   Actionable tips on what files can still be accessed.
*   An **automatic connection check** running every 5 seconds using lightweight network probes to auto-refresh the browser the moment a cellular signal is restored.

---

## 🔌 Comprehensive API Reference

**Base URL**: `http://localhost:5000/api`

### 1. Reverse Location Deciphering
Analyzes latitude and longitude, retrieves regional parameters, and returns inferred farming attributes.
*   **Endpoint**: `GET /api/ai-location`
*   **Query Params**:
    *   `lat` (string, optional - default: `"28.6139"`)
    *   `lon` (string, optional - default: `"77.2090"`)
*   **Response Payload**:
    ```json
    {
      "address": "Azadpur Mandi, Delhi, India",
      "zone": "Indo-Gangetic Plain",
      "soil": "Alluvial Soil",
      "crops": ["Wheat", "Rice", "Maize", "Mustard"]
    }
    ```

### 2. Crop Recommendation Engine
Generates detailed recommendations, compatibility matrix, and warnings.
*   **Endpoint**: `POST /api/recommend-crop`
*   **Headers**: `Content-Type: application/json`
*   **Request Payload**:
    ```json
    {
      "soil_type": "Black Soil",
      "ph": 7.2,
      "temperature": 28,
      "humidity": 65,
      "rainfall": 150,
      "water_source": "Canal Irrigation",
      "location": "Maharashtra",
      "sowing_month": "June",
      "field_notes": "Well-drained with high clay content."
    }
    ```
*   **Response Payload**:
    ```json
    {
      "success": true,
      "data": {
        "primary_recommendation": {
          "crop": "Cotton",
          "confidence": "92%",
          "recommendation_type": "Best",
          "reason_summary": "Highly compatible with deep black soil and June monsoon climate.",
          "issues_detected": [],
          "yield_estimate": "2.5 tons/ha",
          "profit_estimate": "₹80,000 - ₹1,10,000",
          "duration": "180 days",
          "risk_level": "Low",
          "icon": "🌿"
        },
        "suitability_scores": {
          "soil_match": "95%",
          "climate_match": "90%",
          "water_match": "90%"
        },
        "detailed_analysis": {
          "why_this_crop": ["Deep black soil retains moisture essential for cotton taproots", "Temperature fits the 25-35C window"],
          "limitations": ["Susceptible to whitefly if high humidity persists"],
          "action_plan": ["Sow seeds at 2-3 cm depth", "Apply basal fertilizer during tillage"],
          "fertilizer_plan": ["Nitrogen: 80kg/ha", "Phosphorus: 40kg/ha", "Potassium: 40kg/ha"],
          "irrigation_plan": ["Drip irrigation scheduled every 4 days"]
        },
        "alternative_crops": [
          {"crop": "Soybean", "reason": "Shorter duration alternative", "expected_profit": "₹60,000", "risk_level": "Low"}
        ],
        "alerts": []
      }
    }
    ```

### 3. Soil Health Diagnostician
Enters agricultural observations and generates NPK, physical soil composition, and treatment schedules.
*   **Endpoint**: `POST /api/soil-diagnosis`
*   **Headers**: `Content-Type: application/json`
*   **Request Payload**:
    ```json
    {
      "soil_type": "Red Soil",
      "ph": 5.8,
      "location": "Karnataka",
      "field_notes": "Very dry, sandy texture.",
      "temperature": 30,
      "rainfall": 80
    }
    ```
*   **Response Payload**:
    ```json
    {
      "success": true,
      "data": {
        "health_score": "68%",
        "nutrient_status": {
          "nitrogen": "Low",
          "phosphorus": "Low",
          "potassium": "Medium"
        },
        "composition": {
          "sand": "60%",
          "silt": "15%",
          "clay": "25%"
        },
        "diagnosis": "Acidic red soil showing severe nitrogen depletion and dry crusting.",
        "treatment_plan": [
          "Apply agricultural lime to raise soil pH to 6.5",
          "Incorporate 10 tons of organic compost per acre",
          "Inoculate soil with Azotobacter cultures"
        ],
        "biological_health": "Fair",
        "toxicity_risk": "None"
      }
    }
    ```

### 4. Yield & Profit projection
Calculates expected output, revenues, costs, and profits.
*   **Endpoint**: `POST /api/calculate-yield-ai`
*   **Headers**: `Content-Type: application/json`
*   **Request Payload**:
    ```json
    {
      "crop": "Wheat",
      "area": 3,
      "irr": "Tube-well",
      "soil": "Clayey Loam",
      "price": 2400
    }
    ```
*   **Response Payload**:
    ```json
    {
      "yield_qty": 75,
      "revenue": 180000,
      "cost": 45000,
      "profit": 135000,
      "analysis": "Excellent profit margin. Clayey loam offers optimal moisture retention for wheat grains.",
      "yield_boosters": ["Apply urea in three split doses", "Irrigate at Crown Root Initiation stage"],
      "cost_tips": ["Utilize PM-KUSUM solar pumps to save electricity costs"]
    }
    ```

### 5. AI Advisor Simplification
Translates complex scientific advice into simplified, farmer-friendly vernacular terms.
*   **Endpoint**: `POST /api/simplify-recommendation`
*   **Headers**: `Content-Type: application/json`
*   **Request Payload**:
    ```json
    {
      "advice": "Apply mancozeb 75WP fungicide at 2g/L. Drain fields immediately to suppress fungal hyphae expansion."
    }
    ```
*   **Response Payload**:
    ```json
    {
      "simple_explanation": "खेत में जमा फालतू पानी तुरंत बाहर निकालें। बीमारी रोकने के लिए 'मेनकोजेब' दवा 2 ग्राम प्रति लीटर पानी में मिलाकर छिड़काव करें।"
    }
    ```

### 6. Weather & Climate Report
Returns live simulated weather states for the coordinates.
*   **Endpoint**: `GET /api/weather`
*   **Query Params**:
    *   `lat` (string, optional - default: `"28.6139"`)
    *   `lon` (string, optional - default: `"77.2090"`)
*   **Response Payload**:
    ```json
    {
      "current": {
        "temperature": 29,
        "humidity": 58,
        "wind_speed": 14,
        "condition": "Sunny",
        "icon": "☀️",
        "location": "Azadpur"
      },
      "forecast": [
        {
          "day": "Mon",
          "max_temp": 31,
          "min_temp": 25,
          "condition": "Sunny",
          "icon": "☀️"
        }
      ]
    }
    ```

### 7. AI Weather Implication Analyzer
Explains weather hazards, warnings, and schedules.
*   **Endpoint**: `GET /api/analyze-weather`
*   **Query Params**:
    *   `lat` (string)
    *   `lon` (string)
*   **Response Payload**:
    ```json
    {
      "analysis": "Current clear weather is optimal for fertilizer broadcasting. Relative humidity is stable.",
      "tips": ["Complete nitrogen top-dressing today", "Schedule light irrigation before Friday"],
      "alerts": ["No extreme warnings for this week"]
    }
    ```

### 8. Live Market Prices
Retrieves mandi commodity prices.
*   **Endpoint**: `GET /api/mandi-prices`
*   **Response Payload**:
    ```json
    [
      {
        "commodity": "Basmati Rice",
        "market": "Azadpur",
        "state": "Delhi",
        "min": 3500,
        "max": 4500,
        "modal": 4000,
        "trend": "up",
        "change_percent": 5.2
      }
    ]
    ```

### 9. Mandi Price Trend Analytics
Forecasts price movements over 6 months.
*   **Endpoint**: `GET /api/analyze-market`
*   **Query Params**:
    *   `crop` (string, optional - default: `"all"`)
*   **Response Payload**:
    ```json
    {
      "summary": "Wheat prices are experiencing a upward trend due to post-harvest demand spikes.",
      "grow_rec": "Yes",
      "income": "₹45,000 per acre",
      "reasoning": "Global grain supplies are low, boosting export rates.",
      "trend": [2150, 2200, 2250, 2380, 2460, 2550]
    }
    ```

### 10. Welfare Schemes API
Fetches 4 active welfare schemes.
*   **Endpoint**: `GET /api/schemes`
*   **Response Payload**:
    ```json
    [
      {
        "name": "PM-KISAN",
        "icon": "💰",
        "description": "Income support scheme providing ₹6,000 per year in three equal installments.",
        "feature": "Direct Transfer",
        "deadline": "Ongoing",
        "apply_link": "https://pmkisan.gov.in"
      }
    ]
    ```

### 11. Agricultural News Summarizer
Aggregates news items and returns categorized alerts.
*   **Endpoint**: `GET /api/farmer-news`
*   **Response Payload**:
    ```json
    {
      "top_stories": [
        {
          "title": "MSP Increased for Wheat to ₹2,350/quintal",
          "impact": "Positive",
          "detail": "Cabinet approves rate hike for Rabi season.",
          "category": "Market"
        }
      ],
      "summary": "Positive market outlook with strong government backing for Rabi crops."
    }
    ```

### 12. AI Chatbot
Coordinates chats with farmers.
*   **Endpoint**: `POST /api/chatbot`
*   **Headers**: `Content-Type: application/json`
*   **Request Payload**:
    ```json
    {
      "message": "How can I prevent yellow rust in wheat?"
    }
    ```
*   **Response Payload**:
    ```json
    {
      "response": "To control Yellow Rust: 1) Spray Propiconazole (25 EC) at 200ml per acre mixed in 200L of water, 2) Avoid sowing susceptible varieties like HD-2967, 3) Monitor fields daily during cool, humid weather."
    }
    ```

---

## 📦 Installation & Setup

### Prerequisites
*   Python 3.8 or higher installed on your computer.
*   A Groq Cloud API Key (obtainable for free at [console.groq.com](https://console.groq.com)).
*   Git (optional, to clone the project).

### Step 1: Clone the Repository
```bash
git clone https://github.com/parthdahiphale6363-ui/AGRINOVA.git
cd AGRINOVA
```

### Step 2: Set Up a Python Virtual Environment
Initialize an isolated workspace environment:
```bash
# Windows (Command Prompt or PowerShell)
python -m venv venv
.\venv\Scripts\activate

# Linux / MacOS
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Required Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
Create a file named `.env` in the root project folder:
```env
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=agrinova-secret-key-parth-2026
GROQ_API_KEY=your_actual_groq_api_key_here
```

### Step 5: Start the Local Development Server
```bash
python app.py
```
The server will boot up and start listening at **`http://localhost:5000`**. Open this address in your web browser.

---

## ☁️ Deployment & Infrastructure Configurations

The repository contains setup configurations for multiple hosting platforms. 

> [!WARNING]
> Since the project structure hosts `app.py` directly in the root directory (which initializes the backend application by importing `create_app` from the `backend/` folder), build pipelines must compile from the root scope.

### Heroku Setup
*   **Target File**: [Procfile](file:///c:/Users/Asus/Desktop/AGRINOVA-main/Procfile) and [runtime.txt](file:///c:/Users/Asus/Desktop/AGRINOVA-main/runtime.txt)
*   **Definition**: `web: gunicorn app:app`
*   **Instructions**: Heroku installs dependencies from the root `requirements.txt` and calls the `app` instance in `app.py` using gunicorn.

### Railway Setup
*   **Target File**: [railway.json](file:///c:/Users/Asus/Desktop/AGRINOVA-main/railway.json)
*   **Current Configuration**:
    ```json
    "startCommand": "gunicorn backend.app:app"
    ```
*   **Note**: If deploying on Railway, modify the `startCommand` to `gunicorn app:app` (referencing the root file) to prevent import failure.

### Vercel Serverless Setup
*   **Target File**: [vercel.json](file:///c:/Users/Asus/Desktop/AGRINOVA-main/vercel.json)
*   **Current Configuration**:
    ```json
    "src": "backend/app.py",
    "dest": "backend/app.py"
    ```
*   **Note**: If deploying the backend to Vercel Serverless, update the paths to `app.py` in `vercel.json` as there is no `app.py` file located in the `backend/` subdirectory.

---

## 📖 Usage Guide

### Step 1: Initialize Location & Weather Insights
Upon loading the dashboard:
1. Approve the browser's request for location access.
2. The weather widget will auto-populate with local humidity, temperature, and wind speed.
3. Scroll to review the **Groq AI Climate Insight** box to see immediate field action advice based on the forecast.

### Step 2: Request a Crop Recommendation
1. Under the **Crop Recommendation** form, select your soil type (e.g., Alluvial, Black, Sandy).
2. Enter your current pH level (e.g., 6.5) and choose your primary water source.
3. Input the target sowing month and add optional field notes (e.g., "Field has rocky patches").
4. Click **Recommend Crop**. The AI analyzes your parameters and renders the primary recommended crop with a compatibility percentage meter, risk evaluation, and alternative recommendations.

### Step 3: Run a Soil Health Diagnosis
1. Fill in your soil type, pH level, and location in the forms.
2. Under the **Soil Diagnosis** panel, click **Diagnose Soil**.
3. Renders the calculated NPK breakdown, sand/silt/clay physical composition, biological rating, and custom AI Treatment Plan.

### Step 4: Perform a Financial Projection
1. Scroll to the **Yield & Financial Calculator**.
2. Select your crop, acreage, water source, and typical market price per quintal.
3. Click **Calculate Yield**. The system returns expected volume, cost, and net profit margins, accompanied by AI recommendations for lowering operating costs.

### Step 5: Consult the Chatbot
1. Click the floating green chat bubble in the bottom right corner of the dashboard.
2. Enter questions like: *"How do I apply urea to cotton?"* or click one of the quick question chips.
3. The chatbot returns responses streaming from Groq.

---

## 🌾 Supported Crops

AGRINOVA supports detailed mapping for over 23 crop types configured in the utility databases:

| Cereals & Jutes | Pulses | Cash Crops | Perennial & Fruits | Beverages |
| :--- | :--- | :--- | :--- | :--- |
| 🌾 Rice | 🍛 Lentil | 🌿 Cotton | 🥭 Mango | ☕ Coffee |
| 🌾 Wheat | 🥣 Chickpea | 🌱 Soybean | 🍌 Banana | 🍃 Tea |
| 🌽 Maize | 🧶 Kidney Beans | 🍂 Tobacco | 🍇 Grapes | |
| 🧵 Jute | 🌱 Mungbean | | 🍉 Watermelon | |
| | 🌱 Blackgram | | 🍈 Muskmelon | |
| | 🌱 Pigeonpeas | | 🍎 Apple | |
| | 🌱 Mothbeans | | 🍊 Orange | |
| | | | 🥭 Papaya | |
| | | | 🥥 Coconut | |
| | | | 🍎 Pomegranate| |

---

## 🛠️ Developer Reference

### Adding support for a new crop
1. Open [backend/utils/constants.py](file:///c:/Users/Asus/Desktop/AGRINOVA-main/backend/utils/constants.py)
2. Add a new key to the `CROP_INFO` dictionary matching the lowercase name of the crop:
   ```python
   'mustard': {
       'name': 'Mustard', 
       'icon': '🌱', 
       'season': 'Rabi (Oct-Mar)', 
       'water': 'Low', 
       'soil': 'Sandy Loam', 
       'temp': '10-25°C'
   }
   ```
3. The recommendation API will automatically read this database to fetch icons.

### Altering the AI Prompts
*   **Crop Recommendation Logic**: Edit `prompt` inside the `recommend_crop()` function in [farming.py](file:///c:/Users/Asus/Desktop/AGRINOVA-main/backend/api/farming.py).
*   **Soil Diagnostics Logic**: Edit `prompt` in [soil.py](file:///c:/Users/Asus/Desktop/AGRINOVA-main/backend/api/soil.py).
*   **Financial Calculator Logic**: Edit `prompt` in [farming.py](file:///c:/Users/Asus/Desktop/AGRINOVA-main/backend/api/farming.py) under the `calculate_yield_ai()` controller.
*   **Weather Advisor Logic**: Edit `prompt` in [weather.py](file:///c:/Users/Asus/Desktop/AGRINOVA-main/backend/api/weather.py).

---

## 🔮 Future Roadmap
- [ ] Implement user profiles and local SQLite/PostgreSQL databases to save history.
- [ ] Migrate from simulated Mandi data to a live connection with official government Mandi APIs.
- [ ] Add multi-language support (Hindi, Marathi, Punjabi, Tamil, Telugu) for rural accessibility.
- [ ] Integrate local IoT soil moisture and NPK sensor telemetries.
- [ ] Develop native mobile applications using Flutter or React Native.
- [ ] Integrate image recognition APIs for real-time pest and leaf disease identification.

---

## 🤝 Contributing
Contributions make the open-source community an amazing place to learn and build.
1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 📝 License
Distributed under the MIT License. See `LICENSE` for more information.

---

**Happy Farming! 🌾**

*Last Updated: May 2026*
