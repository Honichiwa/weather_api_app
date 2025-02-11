from django.shortcuts import render, redirect
from . import utils
from .forms import CityForm

def index(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            #Takes form input and passes down to get_coordinates func and returns coordinates from geocoding api
            city_cords = utils.get_coordinates(city)

            if city_cords:
                try:
                    latitude, longitude, city_display_name = city_cords
                    #Takes coordinates and returns weather data from weather api
                    data_temps, data_elevation = utils.get_data_from_api(latitude, longitude)
                except Exception as e:
                    data_temps, data_elevation = None, None
                    city_display_name = f"Error fetching data for {city}: {str(e)}"
            else:
                data_temps, data_elevation = None, None
                city_display_name = f'Did not find the "{city}" location, try again'
    else:
        form = CityForm()
        data_temps, data_elevation, city_display_name = None, None, None

    context = {
        "form": form,
        "get_data": data_temps,
        "elevation": data_elevation,
        "city_name": city_display_name,
    }
    return render(request, 'home.html', context=context)