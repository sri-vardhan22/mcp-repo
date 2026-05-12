# Weather MCP Tool

import requests

def get_weather(city):
    """Fetches weather information for a given city."""
    api_key = "your_api_key_here"  # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        print(f"Weather in {city}: {weather}, {temperature}°C")
    else:
        print(f"Failed to get weather data for {city}. Error: {response.status_code}")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)