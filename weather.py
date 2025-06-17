import requests

response = requests.get("https://api.weatherapi.com")
if response.status_code == 200:
    weather_data = response.json()
    
    # Extract useful information
    current_temp = weather_data["current_weather"]["temperature"]
    humidity = weather_data["hourly"]["relative_humidity_2m"][0]  # First hour's humidity
    
    print(f"Current Temperature: {current_temp}°C")
    print(f"Humidity: {humidity}%")
else:
    print(f"Error fetching data: {response.status_code}")