from django.shortcuts import render
from django.contrib import messages
import requests
import datetime


def home(request):

    if  'city' in request.POST:
        city= request.POST['city']
    else:
        city='Bangalore'

    url= f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=93fe1764b88529b8035bd5f6754f8ea5'
    PARAMS= {'units':'metric'}
    
    try:

        data = requests.get(url,params=PARAMS).json()
   
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
   
        day = datetime.date.today()

        return render(request,'index.html',{'description':description , 'icon':icon ,'temp':temp , 'day':day , 'city':city,'exception_occured':False})
    
    except:
        exception_occured=True
        messages.error(request,'Entered data is not available to API')
        day=datetime.date.today()

        return render(request,'index.html',{'description':'clear sky' , 'icon':'01d' ,'temp':'25' , 'day':'day' , 'city':'bangalore','exception_occured':False,})