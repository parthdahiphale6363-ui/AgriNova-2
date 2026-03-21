from backend.app import app

# This file just imports your actual Flask app from the backend folder
# Railway will find this and start correctly

if __name__ == "__main__":
    app.run()