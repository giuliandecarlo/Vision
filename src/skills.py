import requests
import random
import wikipedia
from translate import Translator

NOT_UND_MESS=['Mi spiace, ma al momento non riesco a comprendere ciò che hai detto. Cercherò di migliorare.','Purtroppo ora non sono ancora in grado di capire ciò che hai detto,riprova.']


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


def wikipediaSearch(topic):
    try:
        wikipedia.set_lang("it")
        return(wikipedia.summary(topic,sentences=2))
    except:
        return("C'è stato un errore nella tua ricerca, riprova cercando qualcos'altro.")


def dice():
    num=random.randint(1,6)
    return("Ho lanciato il dado, il numero uscito è "+str(num))

def randNum(numString):
    num=numString.split()
    try:
        n1=int(num[0])
        n2=int(num[2])
        n=random.randint(n1,n2)
        return("Il numero estratto è "+str(n))
    except:
        return("C'è stato un errore. Riprova")

def translate(text):
    try:
        words=text.split()
        print(words)
        message=words[0]
        match(words[2]):
            case 'inglese':
                translator=Translator(from_lang="italian",to_lang="english")
                translation=translator.translate(message)
                return(str(translation))
            case 'spagnolo':
                translator=Translator(from_lang="italian",to_lang="spanish")
                translation=translator.translate(message)
                return(str(translation))
            case 'tedesco':
                translator=Translator(from_lang="italian",to_lang="german")
                translation=translator.translate(message)
                return(str(translation))
            case 'francese':
                translator=Translator(from_lang="italian",to_lang="french")
                translation=translator.translate(message)
                return(str(translation))
            case 'cinese':
                translator=Translator(from_lang="italian",to_lang="chinese")
                translation=translator.translate(message)
                return(str(translation))
            case other:
               return("Mi spiace, c'è stato un errore nella traduzione.") 
    except:
        return("Mi spiace, c'è stato un errore nella traduzione.")

def calculator(text):
    try:
        words=text.split()
        operation=words[1]
        match(operation):
            case '+':
                result=int(words[0])+int(words[2])
                return("Il risultato è: "+str(result))
            case '*':
                result=int(words[0])*int(words[2])
                return("Il risultato è: "+str(result))
            case 'meno':
                result=int(words[0])-int(words[2])
                return("Il risultato è: "+str(result))
            case 'diviso':
                result=int(words[0])/int(words[2])
                return("Il risultato è: "+str(result))
            case other:
                return("C'è stato un problema nel calcolare il risultato, riprova.")
    except:
        return("C'è stato un problema nel calcolare il risultato, riprova.")