from django.shortcuts import render
import requests
import datetime


def home(request):
    if  'city' in request.POST:
        city= request.POST['city']
    else:
        city='Bangalore'
    url= f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=93fe1764b88529b8035bd5f6754f8ea5'
    PARAMS= {'units';'metric'}
    
    return render(request,'weatherapp/index.html')