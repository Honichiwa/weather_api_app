from django.shortcuts import render, redirect
from . import utils
from .forms import CityForm

def index(request):
    data_temps = None
    data_elevation = None
    city_display_name = None
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            city_cords = utils.get_coordinates(city)

            if city_cords:
                city_display_name = city_cords[2]
                latitude = city_cords[0]
                longitude = city_cords[1]
                data = utils.get_data_from_api(latitude, longitude)
                data_temps = data[0]
                data_elevation = data[1]
            else:
                data_temps = None
                data_elevation = None
                city_display_name = f'Did not find the "{city}" location, try again'
    else:
        form = CityForm()
    return render(request, 'home.html', {"form": form, "get_data": data_temps, "elevation" : data_elevation ,"city_name": city_display_name,})