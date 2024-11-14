# weather_app.py

weather_data = {
    "New York": "Sunny, 25°C",
    "Los Angeles": "Cloudy, 20°C",
    "London": "Rainy, 15°C",
    "Paris": "Sunny, 18°C",
}

def get_weather(city):
    return weather_data.get(city, "City not found")

# Sample usage
print("Weather in New York:", get_weather("New York"))
print("Weather in London:", get_weather("London"))
print("Weather in Tokyo:", get_weather("Tokyo"))
