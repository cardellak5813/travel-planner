import requests
import urllib.parse

# Get user input
city = input("Enter a City: ")
country = input("Enter the country or state of the city: ")

# API key and base URL
weatherKey = "e370c1f80781f24e8110649eba4b6329"
base_url = "http://api.openweathermap.org/data/2.5/weather"

# Construct the full API URL
params = {
    'q': f"{city},{country}",
    'appid': weatherKey,
    'units': 'imperial'
}
url = f"{base_url}?{urllib.parse.urlencode(params)}"

# Make the API call
response = requests.get(url)
data = response.json()

# Check if the response contains 'weather' data
if response.status_code == 200 and 'weather' in data:
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    print(f"The weather in {city}, {country} is {weather_description} with a temperature of {temperature}°F.")
else:
    print("Error fetching weather data. Please check the city and country/state names.")