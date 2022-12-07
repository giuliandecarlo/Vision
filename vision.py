import speech_recognition as sp
import pyaudio
import playsound
import os
import random
from gtts import gTTS
import yaml
import datetime
import skills

config = yaml.safe_load(open('config/config.yml', 'rb'))
WAKE_WORDS= ['ciao visione','ciao vision','buongiorno visione','buongiorno vision','buonasera visione','buonasera vision','ehi visione','ehi vision','ok visione','ok vision']
TIME_WORDS= ['ore','orario','che ora è']
WEATHER_WORDS=['che tempo fa ','meteo']
DATE_WORDS=['che giorno è','quante ne abbiamo oggi']
WIKI_WORDS=['fai una ricerca su','parlami di','trova informazioni su']
HOW_MUCH_DAYS_WORDS=['quanto manca al','quanto manca a','quanti giorni mancano al','quanti giorni mancano a']
CLOSE_WORDS=['spegniti','puoi spegnerti','spegnimento']
CLOSE_MESS=['è stato un piacere, a presto.','arrivederci.','perfetto, a presto.']
DICE_WORDS=['lancia un dado','puoi lanciare un dado']
RAND_WORDS=['dimmi un numero casuale tra','estrai un numero tra','estrai un numero casuale tra']


def main():
    while True:
        text_in=getAudio()
        text_in=text_in.lower()
        if (wakeBot(text_in)==True):
            print("Messaggio di wake ricevuto")
            checkSkill(text_in)

        else:
            print("Messaggio di wake non ricevuto")

def response(text):
    print("Vision: "+text)
    tts=gTTS(text=text,lang='it')
    filename="audio.mp3"
    if os.path.exists(filename):
        os.remove(filename)
    tts.save(filename)
    playsound.playsound(filename)
    if os.path.exists(filename):
        os.remove(filename)

def wakeBot(text_in):
    for phrase in WAKE_WORDS:
        if phrase in text_in:
            return True

def closeVocalAssistant():
    print("Vision: In chiusura...")
    ran=random.randrange(len(CLOSE_MESS))
    text_out=CLOSE_MESS[ran]
    response(text_out)
    exit()

def getAudio():
    r=sp.Recognizer()
    with sp.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=0.4)
        result=""
        try:
            print("Vision: Sto ascoltando..")
            audio=r.listen(source)
            result=r.recognize_google(audio,language='it')
            print("User: "+result)
        except Exception as e:
            print("Errore")
    return result

def checkSkill(text_in):
    for phrase in TIME_WORDS:
        if phrase in text_in:
            response(skills.getCurrentTime())
            return

    for phrase in WEATHER_WORDS:
        if phrase in text_in:
            city=text_in.split()[-1]
            response(skills.getWeatherInfo(city))
            return

    for phrase in WIKI_WORDS:
        for phrase1 in WAKE_WORDS:
            if phrase1 in text_in:
                text_in=text_in.replace(phrase1,'')
        if phrase in text_in:
            topic=text_in.replace(phrase,'')
            response(skills.wikipediaSearch(topic))
            return
            
    for phrase in DATE_WORDS:
        if phrase in text_in:
            response(skills.getCurrentDate())
            return

    for phrase in HOW_MUCH_DAYS_WORDS:
        for phrase1 in WAKE_WORDS:
            if phrase1 in text_in:
                text_in=text_in.replace(phrase1,'')
        if phrase in text_in:
            date=text_in.replace(phrase,'')
            response(skills.howManyDays(date))
            return
    
    for phrase in CLOSE_WORDS:
        if phrase in text_in:
            closeVocalAssistant()
    
    for phrase in DICE_WORDS:
        if phrase in text_in:
            response(skills.dice())
            return

    for phrase in RAND_WORDS:
        for phrase1 in WAKE_WORDS:
            if phrase1 in text_in:
                text_in=text_in.replace(phrase1,'')
        if phrase in text_in:
            num=text_in.replace(phrase,'')
            response(skills.randNum(num))
            return

    response(skills.notUnderstand())


if __name__=='__main__':
    try:
        main()
    except:
        print("C'è stato un errore.")
