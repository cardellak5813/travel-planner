import requests
import urllib.parse

city = input("Enter a City: ")
country = input("Enter the country of the city: ")  
key = "e370c1f80781f24e8110649eba4b6329"
url = "http://api.openweathermap.org/geo/1.0/direct?q={city},{country}&limit={5}&appid={key}"

replyData = requests.get(url)
json_data = replyData.json()
print(json_data)