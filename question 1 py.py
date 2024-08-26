import request
import json
import time

# Function to get weather data
def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"
    
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        wind = data["wind"]
        weather_desc = data["weather"][0]["description"]

        # Displaying the weather information
        print(f"City: {city}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Pressure: {main['pressure']} hPa")
        print(f"Weather Description: {weather_desc.capitalize()}")
        print(f"Wind Speed: {wind['speed']} m/s")
        print("-" * 50)
    else:
        print(f"City {city} not found!")

# Main function to monitor weather in real-time
def real_time_weather_monitor(cities, api_key, interval=60):
    while True:
        for city in cities:
            get_weather(city, api_key)
        print(f"Waiting for {interval} seconds before the next update...")
        time.sleep(interval)

if __name__ == "__main__":
    # Replace with your OpenWeatherMap API key
    API_KEY = "your_api_key_here"
    
    # List of cities to monitor
    cities_to_monitor = ["London", "New York", "Tokyo", "Delhi"]

    # Start monitoring the weather
    real_time_weather_monitor(cities_to_monitor, API_KEY, interval=300)  # Update every 5 minutes
