import requests

ApiKey = "e31bae8d59ead35b1fa5f3ad113d1d17"

City = input("City : ")

WeatherData = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={City}&units=imperial&APPID={ApiKey}")

# print(WeatherData.status_code)  # == 200 working fine 

print(WeatherData.json())

print("Weather : ",WeatherData.json()["weather"][0]["main"])

print("Temp : ",WeatherData.json()["main"]['temp'])
print("Min Temp : ",WeatherData.json()["main"]['temp_min'])
print("Max Temp : ",WeatherData.json()["main"]['temp_max'])
print("Humidity : ",WeatherData.json()["main"]['humidity'])