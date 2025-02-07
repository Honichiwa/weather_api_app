import requests
import pandas as pd
from weather_app import local_settings
from weather_app.settings import CACHE_TTL
from django.core.cache import cache

def get_data_from_api(latitude, longitude):

    cache_key = f"weather_{latitude}_{longitude}"
    print(cache_key)
    cached_data = cache.get(cache_key)

    if cached_data:
        time_weather, elevation = cached_data
        return time_weather, elevation
    else:
        # Define API endpoint and parameters
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "hourly": ["temperature_2m", "precipitation_probability", "precipitation"],

        }

        # Make the request
        response = requests.get(url, params=params)
        data = response.json()
        elevation = data['elevation']
        hourly_data = data["hourly"]
        time_weather = {
            time: {
                "temperature_2m": temp,
                "precipitation_probability": prec_prob,
                "precipitation": prec
            }
            for time, temp, prec_prob, prec in zip(
                hourly_data["time"],
                hourly_data["temperature_2m"],
                hourly_data["precipitation_probability"],
                hourly_data["precipitation"]
            )
        }

        cache.set(cache_key, (time_weather, elevation), timeout=CACHE_TTL)

        return time_weather, elevation
#adding for git username test

def get_coordinates(city_name):

    cache_key = f"coordinates_{city_name}"
    cached_data = cache.get(cache_key)

    if cached_data:
        latitude, longitude, display_name = cached_data
        return latitude, longitude, display_name

    url = 'https://nominatim.openstreetmap.org/search?'
    params = {
        'q': city_name,
        'format': 'json',
        'limit': 1
    }
    response = requests.get(url, params=params, headers=local_settings.HEADERS)
    data = response.json()
    if data:
    
        display_name = data[0]['display_name']

        latitude = data[0]['lat']
        longitude = data[0]['lon']

        cache.set(cache_key, (latitude, longitude, display_name), timeout=CACHE_TTL)

        return latitude, longitude, display_name
    
    else:
        return False
