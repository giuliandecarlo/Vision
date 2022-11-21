import speech_recognition as sp
import pyaudio
import playsound
import os
import random
from gtts import gTTS
import yaml
import datetime

config = yaml.safe_load(open('config/config.yml', 'rb'))
WAKE_WORDS= ['ciao vision','ciao visione','buongiorno vision','buongiorno vision','buonasera visione','ehi vision','ehi visione']
DATE_WORDS= ['ore']

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
    for phrase in DATE_WORDS:
        if phrase in text_in:
            getDate()

def getDate():
    now= datetime.datetime.now()
    hour=now.hour
    minute=now.minute
    day_num=now.day
    month_num=now.month
    year=now.year
    if hour=="00":
        text_out="è mezzanotte"
    elif hour=="01":
        text_out="è l'una"
    else:
        text_out="sono le "+str(hour)

    text_out=text_out+" e "+str(minute)+" minuti "
    response(text_out)


if __name__=='__main__':
    try:
        main()
    except:
        print("C'è stato un errore.")
