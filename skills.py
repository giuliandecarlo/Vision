import datetime
import requests
import random
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
    ran=random.randrange(len(NOT_UND_MESS))
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
    months={1:'gennaio',2:'febbraio',3:'marzo',
            4:'aprile',5:'maggio',6:'giugno',
            7:'luglio',8:'agosto',9:'settembre',
            10:'ottobre',11:'novembre',12:'dicembre'}

    text_out=text_out+months[month]
    text_out=text_out+" del "+str(year)
    return(text_out)

def wikipediaSearch(topic):
    try:
        wikipedia.set_lang("it")
        return(wikipedia.summary(topic,sentences=2))
    except:
        return("C'è stato un errore nella tua ricerca, riprova cercando qualcos'altro.")

def howManyDays(date):
    months={'gennaio':1,'febbraio':2,'marzo':3,
            'aprile':4,'maggio':5,'giugno':6,
            'luglio':7,'agosto':8,'settembre':9,
            'ottobre':10,'novembre':11,'dicembre':12}
    try:
        now=datetime.datetime.now()
        today=datetime.date.today()
        if(date.split()[0]=='primo'):
            day=1
        else:
            day=int(date.split()[0])

        month=months[date.split()[1]]
        if(len(date.split())==2):
            if(datetime.date(now.year,month,day)<today):
                year=now.year+1
            else:
                year=now.year
        else:
            year=int(date.split()[2])
        future=datetime.date(year,month,day)
        diff=(future-today).days
        return("Mancano "+str(diff)+" giorni")
    except:
        return("C'è stato un errore nel calcolo dei giorni rimanenti.")

def dice():
    num=random.randint(1,6)
    return("Ho lanciato il dado, il numero uscito è "+str(num))