import speech_recognition as sp
import pyaudio
import os
import random
from gtts import gTTS
import yaml

config = yaml.safe_load(open('config/config.yml', 'rb'))
WAKE_WORDS= ['ciao vision','ciao visione','buongiorno vision','buongiorno vision','buonasera visione','ehi vision','ehi visione']
def main():
    while True:
        text_in=get_audio()
        text_in=text_in.lower()
        if (wakeBot(text_in)==True):
            print("Messaggio di wake ricevuto")
        else:
            print("Messaggio di wake non ricevuto")
    
def wakeBot(text_in):
    for phrase in WAKE_WORDS:
        if phrase in text_in:
            return True

def get_audio():
    r=sp.Recognizer()
    with sp.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=0.4)
        result=""
        try:
            audio=r.listen(source)
            result=r.recognize_google(audio,language='it')
            print("User: "+result)
        except Exception as e:
            print("Errore")
    return result

if __name__=='__main__':
    try:
        main()
    except:
        print("C'è stato un errore.")
