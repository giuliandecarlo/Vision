import datetime
import requests


def getCurrentTime():
    now= datetime.datetime.now()
    hour=now.hour
    minute=now.minute
    if hour=="00":
        text_out="è mezzanotte"
    elif hour=="01":
        text_out="è l'una"
    else:
        text_out="sono le "+str(hour)

    text_out=text_out+" e "+str(minute)+" minuti "
    return(text_out)

def getWeatherInfo(city):
    BASE_URL="http://api.openweathermap.org/data/2.5/weather?"
    API_KEY=open('weather_api.txt','r').read()
    url=BASE_URL+"&lang=it"+"&q="+city+"&appid="+API_KEY
    
    response=requests.get(url).json()
    if(response['cod']==200):
        temp_kelvin= response['main']['temp']
        temp_celsius=temp_kelvin - 273.15
        temp_celsius=int(round(temp_celsius,0))
        description=response['weather'][0]['description']
        text_out="Nella città di "+city+" la temperatura è di circa "+str(temp_celsius)+" gradi e "+description
        return(text_out)
    else:
        return("Mi spiace, ma non trovo la città che stai cercando.")
    

