import datetime
import requests
from random import randrange
import wikipedia

NOT_UND_MESS=['Mi spiace, ma al momento non riesco a comprendere ciò che hai detto. Cercherò di migliorare.','Purtroppo ora non sono ancora in grado di capire ciò che hai detto,riprova.']

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
    
def notUnderstand():
    ran=randrange(len(NOT_UND_MESS))
    text_out=NOT_UND_MESS[ran]
    return(text_out)

def getCurrentDate():
    now= datetime.datetime.now()
    day=now.day
    month=now.month
    year=now.year

    text_out="Oggi è il "
    if day==1:
        text_out=text_out+"primo "
    else:
        text_out=text_out+str(day)+" "
    match month:
        case 1:
            text_out=text_out+"gennaio "
        case 2:
            text_out=text_out+"febbraio "
        case 3:
            text_out=text_out+"marzo "           
        case 4:
            text_out=text_out+"aprile "
        case 5:
            text_out=text_out+"maggio "
        case 6:
            text_out=text_out+"giugno "   
        case 7:
            text_out=text_out+"luglio "
        case 8:
            text_out=text_out+"agosto "
        case 9:
            text_out=text_out+"settembre "
        case 10:
            text_out=text_out+"ottobre "
        case 11:
            text_out=text_out+"novembre "
        case 12:
            text_out=text_out+"dicembre "
        case _:
            text_out=text_out+str(now.month)+" "
    
    text_out=text_out+"del "+str(year)
    return(text_out)

def wikipediaSearch(topic):
    try:
        wikipedia.set_lang("it")
        return(wikipedia.summary(topic,sentences=2))
    except:
        return("C'è stato un errore nella tua ricerca, riprova cercando qualcos'altro.")