# -- coding: utf8 --
import pandas as pd
import requests
from apikeys import API_TOKEN

params = {'q': 'Moscow', "appid": API_TOKEN, 'units': 'metric' }

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params = params)

if response.status_code == 200:
    weather_data = response.json()
    print(weather_data)
    location = weather_data['name']
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    pressure = weather_data["main"]["pressure"]
    weather_description = weather_data["weather"][0]["description"]

    weather_df = pd.DataFrame({
        'Location': [location],
        'Temperature (C)': [temperature],
        'Humidity (N)': [humidity],
        'Pressure ': [pressure],
        'Description': [weather_description]
    })
    print(weather_df)
else:
    print(response.status_code)


