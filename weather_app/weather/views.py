from django.shortcuts import render
from . import utils
from .forms import CityForm

# Create your views here.
def index(request):
    data = None
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            city_cords = utils.get_coordinates(city)
            latitude = city_cords[0]
            longitude = city_cords[1]
            data = utils.get_data_from_api(latitude, longitude)  # Fetch data using user input
    else:
        form = CityForm()
    return render(request, 'home.html', {"form": form, "get_data": data})