from django import forms

class CityForm(forms.Form):
    latitude = forms.DecimalField(label='Latitude', max_digits=8, decimal_places=5)
    longitude = forms.DecimalField(label='Longitude', max_digits=8, decimal_places=5)