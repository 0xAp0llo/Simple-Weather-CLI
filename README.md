# 🌦️ Simple Weather CLI

A simple command line tool that fetches and displays current weather information for any city using the OpenWeatherMap API.

## ✨ Features

- 🌍 Get current weather information for any city
- 🌡️ Display temperature, feels like, weather description, humidity, and wind speed
- 💾 Option to save weather data to a JSON file

## 📋 Requirements

- 🐍 Python 3.6+
- 📦 requests library

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/0xAp0llo/simple-weather-cli.git
cd simple-weather-cli
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Get an API key from [OpenWeatherMap](https://openweathermap.org/api) and replace YOUR_API_KEY in main.py with your actual API key.

## 🔍 Usage
```bash
python main.py <city_name> [options]
```

## ⚙️ Options

-s, --save: Save weather data to a JSON file

## 📝 Examples

Get weather for London
```bash
python main.py London
```

Get weather for New York and save to file
```bash
python main.py "New York" -s
```

## 📊 Example Output

Weather in London, GB
Date & Time: 2023-09-10 12:34:56

Temperature: 18.5°C
Feels like: 17.9°C
Weather: Partly cloudy
Humidity: 72%
Wind Speed: 4.12 m/s

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
