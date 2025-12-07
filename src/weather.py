import os
import requests
from dotenv import load_dotenv

# Load the secret keys from the .env file
load_dotenv()

def get_weather(city: str) -> dict:
    """
    Fetches the current weather for a specific city.
    Returns a dictionary with temperature, description, and city name.
    """
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        return {"error": "API Key not found. Check your .env file."}

    # API Endpoint for OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"

    try:
        response = requests.get(url)
        
        # Check if the city was found (200 means OK)
        if response.status_code == 200:
            data = response.json()
            return {
                "city": data["name"],
                "temp": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"]
            }
        elif response.status_code == 404:
            return {"error": f"City '{city}' not found."}
        else:
            return {"error": f"API Error: {response.status_code}"}

    except requests.exceptions.RequestException as e:
        return {"error": f"Connection Error: {e}"}

# This allows us to test this file directly by running it alone
if __name__ == "__main__":
    # Test with Cincinnati
    print(get_weather("Cincinnati"))