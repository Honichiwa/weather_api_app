import requests
import pandas as pd
from weather_app import local_settings
from weather_app.settings import CACHE_TTL
from django.core.cache import cache

def get_data_from_api(latitude, longitude):
    """
    Fetches weather data from the Open-Meteo API for the given latitude and longitude.

    Returns:
    A tuple containing a dictionary of time-temperature pairs and the elevation.
    """
    #Checks if the coordinates you are searching for is in redis cache
    cache_key = f"weather_{latitude}_{longitude}"
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
        #Caches the weather information of the coordinates for specified time: CACHE_TTL
        cache.set(cache_key, (time_weather, elevation), timeout=CACHE_TTL)

        return time_weather, elevation

def get_coordinates(city_name):
    """
    Fetches coordinates for a given city name using the Nominatim API.

    Returns:
    A tuple containing latitude, longitude, and display name if found, else None.
    """
    #Checks if the city you are searching for is in redis cache
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
    # HEADERS == {'User-Agent' : 'yourProjectName1.0 (your.email@.email.com)'}
    response = requests.get(url, params=params, headers=local_settings.HEADERS)
    data = response.json()

    if data:
        display_name = data[0]['display_name']
        latitude = float(data[0]['lat'])
        longitude = float(data[0]['lon'])
        #Caches the coordinates of the searched city for specified time: CACHE_TTL
        cache.set(cache_key, (latitude, longitude, display_name), timeout=CACHE_TTL)
        
        return latitude, longitude, display_name
    else:
        return False
