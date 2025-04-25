import requests
import argparse
import json
from datetime import datetime

API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """
    Get weather information for a specified city
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        
        data = response.json()
        display_weather(data)
        return data
        
    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            print(f"City '{city}' not found!")
        else:
            print(f"Error: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")

def display_weather(data):
    """
    Display formatted weather information
    """
    city = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    dt = datetime.fromtimestamp(data["dt"])
    
    print("\n" + "="*50)
    print(f"Weather in {city}, {country}")
    print(f"Date & Time: {dt.strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*50)
    print(f"Temperature: {temp}°C")
    print(f"Feels like: {feels_like}°C")
    print(f"Weather: {description.capitalize()}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print("="*50 + "\n")

def save_to_file(data, filename="weather_data.json"):
    """
    Save weather data to JSON file
    """
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Weather data saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Get current weather for a city")
    parser.add_argument("city", help="City name (e.g., 'London', 'New York')")
    parser.add_argument("-s", "--save", action="store_true", help="Save data to file")
    
    args = parser.parse_args()
    
    data = get_weather(args.city)
    
    if data and args.save:
        save_to_file(data)

if __name__ == "__main__":
    main()
