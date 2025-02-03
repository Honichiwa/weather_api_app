import requests
import pandas as pd

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
    new_data = zip(data['hourly']['time'], data['hourly']['temperature_2m'])
    time_temp = { k:v for (k,v) in new_data}

    return time_temp

# def get_data():
#     with open("test.json", "r") as file:
#         data = json.load(file)

#     new_data = zip(data['hourly']['time'], data['hourly']['temperature_2m'])

#     time_temp = { k:v for (k,v) in new_data}

#     return time_temp
