CROP_INFO = {
    # Cereals
    'rice': {'name': 'Rice', 'icon': '🌾', 'season': 'Kharif (June-Nov)', 'water': 'High (Standing Water)', 'soil': 'Clay/Clayey Loam', 'temp': '20-35°C'},
    'wheat': {'name': 'Wheat', 'icon': '🌾', 'season': 'Rabi (Nov-April)', 'water': 'Medium (4-6 Irrigations)', 'soil': 'Silty Loam', 'temp': '15-25°C'},
    'maize': {'name': 'Maize', 'icon': '🌽', 'season': 'Kharif/Rabi', 'water': 'Medium', 'soil': 'Well-drained Loam', 'temp': '22-30°C'},
    'jowar': {'name': 'Jowar (Sorghum)', 'icon': '🌾', 'season': 'Kharif/Rabi', 'water': 'Low-Medium', 'soil': 'Loam', 'temp': '20-35°C'},
    'bajra': {'name': 'Bajra (Pearl Millet)', 'icon': '🌾', 'season': 'Kharif', 'water': 'Very Low', 'soil': 'Sandy to Sandy Loam', 'temp': '25-35°C'},
    'ragi': {'name': 'Ragi (Finger Millet)', 'icon': '🌾', 'season': 'Kharif/Rabi', 'water': 'Low-Medium', 'soil': 'Sandy Loam', 'temp': '18-28°C'},
    
    # Pulses
    'chickpea': {'name': 'Chickpea', 'icon': '🥣', 'season': 'Rabi', 'water': 'Low', 'soil': 'Diverse Loams', 'temp': '15-25°C'},
    'lentil': {'name': 'Lentil', 'icon': '🍛', 'season': 'Rabi', 'water': 'Low', 'soil': 'Diverse Loams', 'temp': '18-30°C'},
    'arhar': {'name': 'Arhar (Pigeon Pea)', 'icon': '🌱', 'season': 'Kharif', 'water': 'Low-Medium', 'soil': 'Well-drained Loam', 'temp': '20-30°C'},
    'mungbean': {'name': 'Mungbean', 'icon': '🌱', 'season': 'Kharif/Summer', 'water': 'Low', 'soil': 'Loamy to Sandy Loam', 'temp': '25-35°C'},
    'blackgram': {'name': 'Blackgram (Urad)', 'icon': '🌱', 'season': 'Kharif', 'water': 'Low', 'soil': 'Heavy Clay', 'temp': '25-35°C'},
    'masoor': {'name': 'Masoor (Masur)', 'icon': '🍛', 'season': 'Rabi', 'water': 'Low', 'soil': 'Well-drained Loam', 'temp': '15-20°C'},
    'pigeonpeas': {'name': 'Pigeonpeas', 'icon': '🌱', 'season': 'Kharif', 'water': 'Low', 'soil': 'Well-drained Loam', 'temp': '20-30°C'},
    'mothbeans': {'name': 'Mothbeans', 'icon': '🌱', 'season': 'Kharif/Summer', 'water': 'Very Low', 'soil': 'Sandy', 'temp': '25-35°C'},
    'kidneybeans': {'name': 'Kidney Beans', 'icon': '🧶', 'season': 'Rabi/Kharif', 'water': 'Medium', 'soil': 'Deep Silty Loam', 'temp': '15-25°C'},
    
    # Cash Crops
    'cotton': {'name': 'Cotton', 'icon': '🌿', 'season': 'Kharif (May-Oct)', 'water': 'Medium', 'soil': 'Deep Black Soil', 'temp': '25-35°C'},
    'jute': {'name': 'Jute', 'icon': '🧵', 'season': 'Kharif', 'water': 'High', 'soil': 'New Alluvial', 'temp': '24-34°C'},
    'tobacco': {'name': 'Tobacco', 'icon': '🍂', 'season': 'Rabi', 'water': 'Medium', 'soil': 'Sandy Loam', 'temp': '20-30°C'},
    'sugarcane': {'name': 'Sugarcane', 'icon': '🌾', 'season': 'Annual', 'water': 'High', 'soil': 'Deep Loam', 'temp': '20-30°C'},
    
    # Oilseeds
    'groundnut': {'name': 'Groundnut', 'icon': '🥜', 'season': 'Kharif/Rabi', 'water': 'Medium', 'soil': 'Sandy Loam', 'temp': '20-30°C'},
    'sunflower': {'name': 'Sunflower', 'icon': '🌻', 'season': 'Kharif/Rabi', 'water': 'Medium', 'soil': 'Well-drained Loam', 'temp': '20-28°C'},
    'soybean': {'name': 'Soybean', 'icon': '🌱', 'season': 'Kharif', 'water': 'Medium', 'soil': 'Well-drained Loam', 'temp': '20-30°C'},
    'mustard': {'name': 'Mustard', 'icon': '🌾', 'season': 'Rabi', 'water': 'Low', 'soil': 'Sandy Loam', 'temp': '15-25°C'},
    'sesamum': {'name': 'Sesamum (Sesame)', 'icon': '🌾', 'season': 'Kharif', 'water': 'Low-Medium', 'soil': 'Loamy', 'temp': '24-28°C'},
    'safflower': {'name': 'Safflower', 'icon': '🌻', 'season': 'Rabi', 'water': 'Low', 'soil': 'Deep Well-drained', 'temp': '18-24°C'},
    
    # Fruits
    'mango': {'name': 'Mango', 'icon': '🥭', 'season': 'Perennial', 'water': 'Low/Medium', 'soil': 'Deep Loamy', 'temp': '24-30°C'},
    'banana': {'name': 'Banana', 'icon': '🍌', 'season': 'Year-round', 'water': 'Very High', 'soil': 'Rich Volcanic/Alluvial', 'temp': '20-30°C'},
    'papaya': {'name': 'Papaya', 'icon': '🥭', 'season': 'Year-round', 'water': 'Medium', 'soil': 'Well-drained Rich', 'temp': '25-30°C'},
    'coconut': {'name': 'Coconut', 'icon': '🥥', 'season': 'Perennial', 'water': 'High', 'soil': 'Sandy/Alluvial', 'temp': '20-30°C'},
    'orange': {'name': 'Orange', 'icon': '🍊', 'season': 'Year-round', 'water': 'Medium', 'soil': 'Light Loamy', 'temp': '13-37°C'},
    'lemon': {'name': 'Lemon', 'icon': '🍋', 'season': 'Year-round', 'water': 'Medium', 'soil': 'Well-drained Loam', 'temp': '15-35°C'},
    'grapes': {'name': 'Grapes', 'icon': '🍇', 'season': 'Dec-May', 'water': 'Medium', 'soil': 'Sandy Loam', 'temp': '15-35°C'},
    'apple': {'name': 'Apple', 'icon': '🍎', 'season': 'Rabi (Oct-Feb)', 'water': 'Medium', 'soil': 'Well-drained Loam', 'temp': '10-25°C'},
    'pomegranate': {'name': 'Pomegranate', 'icon': '🍎', 'season': 'Year-round', 'water': 'Low', 'soil': 'Diverse (Well-drained)', 'temp': '25-35°C'},
    'guava': {'name': 'Guava', 'icon': '🥭', 'season': 'Year-round', 'water': 'Low-Medium', 'soil': 'Well-drained Loam', 'temp': '20-35°C'},
    'pineapple': {'name': 'Pineapple', 'icon': '🍍', 'season': 'Year-round', 'water': 'Medium', 'soil': 'Sandy Loam', 'temp': '20-30°C'},
    'strawberry': {'name': 'Strawberry', 'icon': '🍓', 'season': 'Rabi', 'water': 'Medium', 'soil': 'Well-drained Sandy Loam', 'temp': '15-25°C'},
    'litchi': {'name': 'Litchi', 'icon': '🍒', 'season': 'Winter', 'water': 'Medium', 'soil': 'Well-drained Loam', 'temp': '15-25°C'},
    'kiwi': {'name': 'Kiwi', 'icon': '🥝', 'season': 'Rabi', 'water': 'Medium', 'soil': 'Well-drained Loam', 'temp': '10-20°C'},
    
    # Spices & Herbs
    'turmeric': {'name': 'Turmeric', 'icon': '🌾', 'season': 'Kharif', 'water': 'Medium', 'soil': 'Rich Well-drained Loam', 'temp': '20-30°C'},
    'ginger': {'name': 'Ginger', 'icon': '🌾', 'season': 'Kharif', 'water': 'Medium-High', 'soil': 'Rich Well-drained', 'temp': '20-30°C'},
    'chili': {'name': 'Chili', 'icon': '🌶️', 'season': 'Rabi/Kharif', 'water': 'Medium', 'soil': 'Well-drained Loam', 'temp': '20-30°C'},
    'cumin': {'name': 'Cumin', 'icon': '🌾', 'season': 'Rabi', 'water': 'Low-Medium', 'soil': 'Well-drained Loam', 'temp': '18-25°C'},
    'coriander': {'name': 'Coriander', 'icon': '🌿', 'season': 'Rabi', 'water': 'Low', 'soil': 'Well-drained Loam', 'temp': '15-25°C'},
    'cardamom': {'name': 'Cardamom', 'icon': '🌿', 'season': 'Perennial', 'water': 'High', 'soil': 'Rich Forest Soil', 'temp': '15-35°C'},
    'fenugreek': {'name': 'Fenugreek (Methi)', 'icon': '🌱', 'season': 'Rabi', 'water': 'Low-Medium', 'soil': 'Loam', 'temp': '15-25°C'},
    'mint': {'name': 'Mint', 'icon': '🌿', 'season': 'Year-round', 'water': 'Medium', 'soil': 'Moist Loam', 'temp': '15-30°C'},
    'asafoetida': {'name': 'Asafoetida', 'icon': '🌾', 'season': 'Rabi', 'water': 'Low', 'soil': 'Well-drained', 'temp': '15-25°C'},
    'clove': {'name': 'Clove', 'icon': '🌿', 'season': 'Perennial', 'water': 'High', 'soil': 'Rich Well-drained', 'temp': '20-30°C'},
    'garlic': {'name': 'Garlic', 'icon': '🧄', 'season': 'Rabi', 'water': 'Medium', 'soil': 'Sandy Loam', 'temp': '15-25°C'},
    'onion': {'name': 'Onion', 'icon': '🧅', 'season': 'Rabi', 'water': 'Medium', 'soil': 'Well-drained Loam', 'temp': '13-24°C'},
    
    # Vegetables
    'tomato': {'name': 'Tomato', 'icon': '🍅', 'season': 'Rabi/Summer', 'water': 'Medium', 'soil': 'Well-drained Loam', 'temp': '20-30°C'},
    'potato': {'name': 'Potato', 'icon': '🥔', 'season': 'Rabi', 'water': 'Medium', 'soil': 'Well-drained Loam', 'temp': '15-20°C'},
    'cabbage': {'name': 'Cabbage', 'icon': '🥬', 'season': 'Rabi', 'water': 'Medium', 'soil': 'Rich Loam', 'temp': '10-25°C'},
    'cauliflower': {'name': 'Cauliflower', 'icon': '🥦', 'season': 'Rabi', 'water': 'Medium', 'soil': 'Rich Loam', 'temp': '15-25°C'},
    'carrot': {'name': 'Carrot', 'icon': '🥕', 'season': 'Rabi', 'water': 'Low-Medium', 'soil': 'Sandy Loam', 'temp': '10-25°C'},
    'brinjal': {'name': 'Brinjal (Eggplant)', 'icon': '🍆', 'season': 'Rabi/Summer', 'water': 'Medium', 'soil': 'Well-drained Loam', 'temp': '25-30°C'},
    'okra': {'name': 'Okra (Ladyfinger)', 'icon': '🌾', 'season': 'Kharif/Summer', 'water': 'Medium', 'soil': 'Well-drained Loam', 'temp': '25-35°C'},
    'cucumber': {'name': 'Cucumber', 'icon': '🥒', 'season': 'Kharif/Summer', 'water': 'Medium-High', 'soil': 'Well-drained Loam', 'temp': '20-30°C'},
    'pumpkin': {'name': 'Pumpkin', 'icon': '🎃', 'season': 'Kharif/Summer', 'water': 'Medium', 'soil': 'Well-drained Loam', 'temp': '20-30°C'},
    'spinach': {'name': 'Spinach', 'icon': '🥬', 'season': 'Rabi', 'water': 'Medium', 'soil': 'Rich Loam', 'temp': '10-25°C'},
    'beans': {'name': 'Beans', 'icon': '🫘', 'season': 'Kharif/Rabi', 'water': 'Medium', 'soil': 'Well-drained Loam', 'temp': '18-28°C'},
    'pepper': {'name': 'Bell Pepper', 'icon': '🌶️', 'season': 'Rabi', 'water': 'Medium', 'soil': 'Well-drained Loam', 'temp': '20-30°C'},
    
    # Melons
    'watermelon': {'name': 'Watermelon', 'icon': '🍉', 'season': 'Summer (Feb-June)', 'water': 'Medium', 'soil': 'Sandy to Sandy Loam', 'temp': '24-30°C'},
    'muskmelon': {'name': 'Muskmelon', 'icon': '🍈', 'season': 'Summer', 'water': 'Medium', 'soil': 'Sandy Loam', 'temp': '24-30°C'},
    
    # Plantation Crops
    'coffee': {'name': 'Coffee', 'icon': '☕', 'season': 'Perennial', 'water': 'High', 'soil': 'Deep Rich Loam', 'temp': '15-28°C'},
    'tea': {'name': 'Tea', 'icon': '🍃', 'season': 'Perennial', 'water': 'High', 'soil': 'Acidic Forest Soil', 'temp': '13-32°C'},
    'arecanut': {'name': 'Arecanut (Betel Nut)', 'icon': '🌴', 'season': 'Perennial', 'water': 'High', 'soil': 'Rich Well-drained', 'temp': '20-30°C'},
    'rubber': {'name': 'Rubber', 'icon': '🌳', 'season': 'Perennial', 'water': 'High', 'soil': 'Well-drained Laterite', 'temp': '20-30°C'},
}

MARKET_PRICES = [
    # Northern Region - Punjab & Haryana
    {'commodity': 'Basmati Rice', 'market': 'Azadpur', 'state': 'Delhi', 'min': 3500, 'max': 4500, 'modal': 4000, 'trend': 'up', 'change_percent': 5.2},
    {'commodity': 'Common Rice', 'market': 'Bathinda', 'state': 'Punjab', 'min': 1800, 'max': 2200, 'modal': 2000, 'trend': 'stable', 'change_percent': 0.5},
    {'commodity': 'Wheat', 'market': 'Khanna', 'state': 'Punjab', 'min': 2400, 'max': 2700, 'modal': 2550, 'trend': 'stable', 'change_percent': 0.1},
    {'commodity': 'Wheat', 'market': 'Hisar', 'state': 'Haryana', 'min': 2350, 'max': 2650, 'modal': 2500, 'trend': 'up', 'change_percent': 1.2},
    {'commodity': 'Maize', 'market': 'Karnal', 'state': 'Haryana', 'min': 1750, 'max': 2050, 'modal': 1900, 'trend': 'down', 'change_percent': 2.1},
    {'commodity': 'Cotton', 'market': 'Ludhiana', 'state': 'Punjab', 'min': 5900, 'max': 6400, 'modal': 6150, 'trend': 'up', 'change_percent': 2.8},
    {'commodity': 'Potato', 'market': 'Fazilka', 'state': 'Punjab', 'min': 1200, 'max': 1800, 'modal': 1500, 'trend': 'down', 'change_percent': 8.5},
    
    # Central Region - Madhya Pradesh & Chhattisgarh
    {'commodity': 'Soybean', 'market': 'Indore', 'state': 'MP', 'min': 4200, 'max': 4800, 'modal': 4500, 'trend': 'up', 'change_percent': 1.5},
    {'commodity': 'Gram (Chickpea)', 'market': 'Indore', 'state': 'MP', 'min': 5200, 'max': 6000, 'modal': 5600, 'trend': 'up', 'change_percent': 3.2},
    {'commodity': 'Maize', 'market': 'Gultekdi', 'state': 'MS', 'min': 1800, 'max': 2100, 'modal': 1950, 'trend': 'down', 'change_percent': 2.5},
    {'commodity': 'Cotton', 'market': 'APMC Gujarat', 'state': 'GJ', 'min': 5800, 'max': 6400, 'modal': 6100, 'trend': 'up', 'change_percent': 3.8},
    {'commodity': 'Mustard', 'market': 'Chhatarpur', 'state': 'MP', 'min': 4500, 'max': 5200, 'modal': 4850, 'trend': 'up', 'change_percent': 2.3},
    {'commodity': 'Garlic', 'market': 'Mandsaur', 'state': 'MP', 'min': 3000, 'max': 4000, 'modal': 3500, 'trend': 'stable', 'change_percent': 0.8},
    
    # Western Region - Gujarat & Rajasthan
    {'commodity': 'Groundnut', 'market': 'Junagadh', 'state': 'GJ', 'min': 5000, 'max': 6000, 'modal': 5500, 'trend': 'up', 'change_percent': 4.1},
    {'commodity': 'Cumin', 'market': 'Unjha', 'state': 'GJ', 'min': 12000, 'max': 15000, 'modal': 13500, 'trend': 'up', 'change_percent': 5.6},
    {'commodity': 'Onion', 'market': 'Nashik', 'state': 'MS', 'min': 1500, 'max': 2500, 'modal': 2000, 'trend': 'down', 'change_percent': 10.2},
    {'commodity': 'Chili', 'market': 'Guntur', 'state': 'AP', 'min': 8000, 'max': 12000, 'modal': 10000, 'trend': 'down', 'change_percent': 6.8},
    {'commodity': 'Turmeric', 'market': 'Nizamabad', 'state': 'TG', 'min': 6000, 'max': 8000, 'modal': 7000, 'trend': 'up', 'change_percent': 4.3},
    
    # Eastern Region - West Bengal & Bihar
    {'commodity': 'Jute', 'market': 'Murshidabad', 'state': 'WB', 'min': 3500, 'max': 4500, 'modal': 4000, 'trend': 'down', 'change_percent': 3.2},
    {'commodity': 'Paddy (Rice)', 'market': 'Gaya', 'state': 'Bihar', 'min': 1600, 'max': 2000, 'modal': 1800, 'trend': 'stable', 'change_percent': 0.3},
    {'commodity': 'Sugarcane', 'market': 'Bijnor', 'state': 'UP', 'min': 300, 'max': 400, 'modal': 350, 'trend': 'stable', 'change_percent': 0.2},
    {'commodity': 'Lentil', 'market': 'Arrah', 'state': 'Bihar', 'min': 6500, 'max': 7500, 'modal': 7000, 'trend': 'up', 'change_percent': 2.1},
    
    # Southern Region - Karnataka, Tamil Nadu & Andhra Pradesh
    {'commodity': 'Tomato', 'market': 'Kolar', 'state': 'KA', 'min': 600, 'max': 1200, 'modal': 900, 'trend': 'down', 'change_percent': 12.0},
    {'commodity': 'Coffee', 'market': 'Chikmagalur', 'state': 'KA', 'min': 8000, 'max': 11000, 'modal': 9500, 'trend': 'down', 'change_percent': 3.5},
    {'commodity': 'Coconut', 'market': 'Kanyakumari', 'state': 'TN', 'min': 8000, 'max': 12000, 'modal': 10000, 'trend': 'up', 'change_percent': 2.8},
    {'commodity': 'Coriander', 'market': 'Salem', 'state': 'TN', 'min': 3500, 'max': 4500, 'modal': 4000, 'trend': 'stable', 'change_percent': 0.6},
    {'commodity': 'Black Pepper', 'market': 'Kochi', 'state': 'KL', 'min': 25000, 'max': 35000, 'modal': 30000, 'trend': 'up', 'change_percent': 1.9},
    {'commodity': 'Cardamom', 'market': 'Idukki', 'state': 'KL', 'min': 200000, 'max': 250000, 'modal': 225000, 'trend': 'down', 'change_percent': 4.2},
    
    # Additional Premium Commodities
    {'commodity': 'Cashew', 'market': 'Kodungallur', 'state': 'KL', 'min': 12000, 'max': 16000, 'modal': 14000, 'trend': 'up', 'change_percent': 1.8},
    {'commodity': 'Tea', 'market': 'Siliguri', 'state': 'WB', 'min': 100, 'max': 300, 'modal': 200, 'trend': 'stable', 'change_percent': 0.5},
    {'commodity': 'Ginger', 'market': 'Erode', 'state': 'TN', 'min': 4000, 'max': 6000, 'modal': 5000, 'trend': 'up', 'change_percent': 3.1},
    {'commodity': 'Arhar (Dal)', 'market': 'Madhya Pradesh', 'state': 'MP', 'min': 6500, 'max': 7800, 'modal': 7150, 'trend': 'up', 'change_percent': 2.5},
]
