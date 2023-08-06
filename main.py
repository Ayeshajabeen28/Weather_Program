import requests

def get_weather_data(api_key, city):
    """
    Get weather data for the given city using the OpenWeatherMap API.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Change to "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: Unable to fetch weather data for {city}")
        return None

def display_weather_data(data):
    """
    Display the weather data.
    """
    if data is None:
        return

    name = data["name"]
    weather = data["weather"][0]["main"]
    description = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    print(f"Weather for {name}:")
    print(f"Description: {description}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

if __name__ == "__main__":
    # Replace "YOUR_API_KEY" with your actual OpenWeatherMap API key
    api_key = "YOUR_API_KEY"
    
    city = input("Enter the city name: ")
    weather_data = get_weather_data(api_key, city)

    if weather_data:
        display_weather_data(weather_data)
