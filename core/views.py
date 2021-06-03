from django.shortcuts import render
import requests

# Create your views here.


def index(request):
    if request.method == 'POST':
        lat = request.POST.get('lat')
        lon = request.POST.get('lon')

    else:
        lat = 51.5
        lon = -0.25
    url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={}&lon={}'.format(lat, lon)
    weather_data = requests.get(url).json()
    return render(request, 'core/index.html', context={
        'data': weather_data
    })
