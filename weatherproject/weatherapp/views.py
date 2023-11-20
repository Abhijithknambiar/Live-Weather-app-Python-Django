from django.shortcuts import render
from django.contrib import messages
#import request
import datetime


def home(request):

    if  'city' in request.POST:
        city= request.POST['city']
    else:
        city='Bangalore'

    url= f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=93fe1764b88529b8035bd5f6754f8ea5'
    PARAMS= {'units':'metric'}
    
    data = request.get(url,params=PARAMS).json()
    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']
    day = datetime.date.today()

    return render(request,'weatherapp/index.html' , {'description':description , 'icon':icon ,'temp':temp , 'day':day , 'city':city})