import requests

apikey = ""
city = "London"
url = f"http://api.weatherapi.com/v1/current.json?key={apikey}&q={city}&aqi=no"
response = requests.get(url)
weatherapi_json = response.json()
temp = weatherapi_json.get('current').get('temp_c')
description = weatherapi_json.get('current').get('condition').get('text')
print(f"Today the weather in {city} is {description} and {temp} degrees")