import requests

api_key = "9264a5484ef25e746b733acde880cab0"
city_name = input("Please Enter The Name Of City: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&APPID={api_key}")

#print(weather_data.json())

weather = weather_data.json()['weather'][0]['description']
temp = weather_data.json()['main']['temp']
feels = weather_data.json()['main']['feels_like']
humidity = weather_data.json()['main']['humidity']
feels = int((feels-32) * (5/9))
temp = int((temp-32)*(5/9))
print(f"Conditions: {weather}\nTemperature: {temp} DEGREE CELSIUS\nFeels Like: {feels} DEGREE CELSIUS\nHumidity Level: {humidity}%")
