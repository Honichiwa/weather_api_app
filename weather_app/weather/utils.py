import requests
import pandas as pd
from weather_app import local_settings

def get_data_from_api(latitude, longitude):
# Define API endpoint and parameters
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
	    "longitude": longitude,
        "hourly": "temperature_2m"
    }

    # Make the request
    response = requests.get(url, params=params)
    data = response.json()
    elevation = data['elevation']
    new_data = zip(data['hourly']['time'], data['hourly']['temperature_2m'])
    time_temp = { k:v for (k,v) in new_data}

    return time_temp, elevation

def get_coordinates(city_name):
    url = 'https://nominatim.openstreetmap.org/search?'
    params = {
        'q': city_name,
        'format': 'json',
        'limit': 1
    }
    response = requests.get(url, params=params, headers=local_settings.HEADERS)
    data = response.json()
    
    latitude = data[0]['lat']
    longitude = data[0]['lon']

    return latitude, longitude

# def get_data():
#     with open("test.json", "r") as file:
#         data = json.load(file)

#     new_data = zip(data['hourly']['time'], data['hourly']['temperature_2m'])

#     time_temp = { k:v for (k,v) in new_data}

#     return time_temp
