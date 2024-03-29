import speech_recognition as sp
import pyaudio
import playsound
import os
import random
from gtts import gTTS
import yaml
import datetime
import skills
import shoppingList,pcUtilities,dateAndTime,openLinks,exchangeRate
from configWords import *
#config = yaml.safe_load(open('config/config.yml', 'rb'))

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
            response(dateAndTime.getCurrentTime())
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
            response(dateAndTime.getCurrentDate())
            return

    for phrase in HOW_MUCH_DAYS_WORDS:
        for phrase1 in WAKE_WORDS:
            if phrase1 in text_in:
                text_in=text_in.replace(phrase1,'')
        if phrase in text_in:
            date=text_in.replace(phrase,'')
            response(dateAndTime.howManyDays(date))
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

    for phrase in OFF_WORDS:
        if phrase in text_in:
            response("Perfetto,inserisci la password e il sistema si spegnerà.")
            pcUtilities.shutdownDevice()
            return

    for phrase in RESTART_WORDS:
        if phrase in text_in:
            response("Perfetto,inserisci la password e il sistema si riavvierà.")
            pcUtilities.restartDevice()
            return

    for phrase in BATTERY_WORDS:
        if phrase in text_in:
            response(pcUtilities.batteryInfo())
            return 

    for phrase in TRANSLATE_WORDS:
        for phrase1 in WAKE_WORDS:
            if phrase1 in text_in:
                text_in=text_in.replace(phrase1,'')
        if phrase in text_in:
            text=text_in.replace(phrase,'')
            response(skills.translate(text))
            return    

    for phrase in CALCULATOR_WORDS:
        for phrase1 in WAKE_WORDS:
            if phrase1 in text_in:
                text_in=text_in.replace(phrase1,'')
        if phrase in text_in:
            text=text_in.replace(phrase,'')
            response(skills.calculator(text))
            return  

    for phrase in ADD_LIST_WORDS:
        for phrase1 in WAKE_WORDS:
            if phrase1 in text_in:
                text_in=text_in.replace(phrase1,'')
        if phrase in text_in:
            text=text_in.replace(phrase,'')
            response(shoppingList.addList(text))
            return

    for phrase in REMOVE_ALL_LIST_WORDS:
        for phrase1 in WAKE_WORDS:
            if phrase1 in text_in:
                text_in=text_in.replace(phrase1,'')
        if phrase in text_in:
            text=text_in.replace(phrase,'')
            response(shoppingList.removeAll())
            return

    for phrase in REMOVE_LIST_EL_WORDS:
        for phrase1 in WAKE_WORDS:
            if phrase1 in text_in:
                text_in=text_in.replace(phrase1,'')
        if phrase in text_in:
            text=text_in.replace(phrase,'')
            response(shoppingList.removeList(text))
            return


    for phrase in GET_LIST_WORDS:
        if phrase in text_in:
            response(shoppingList.getList())
            return 

    for phrase in RICK_ROLL_WORDS:
        if phrase in text_in:
            openLinks.rickRoll()
            return 

    for phrase in YT_SEARCH_WORDS:
        for phrase1 in WAKE_WORDS:
            if phrase1 in text_in:
                text_in=text_in.replace(phrase1,'')
        if phrase in text_in:
            text=text_in.replace(phrase,'')
            response("Avvio la ricerca, ecco il risultato: ")
            openLinks.ytSearch(text)
            return

    for phrase in YT_PLAY_WORDS:
        for phrase1 in WAKE_WORDS:
            if phrase1 in text_in:
                text_in=text_in.replace(phrase1,'')
        if phrase in text_in:
            text=text_in.replace(phrase,'')
            response("Avvio la riproduzione, ecco il risultato: ")
            openLinks.ytPlay(text)
            return

    for phrase in EXCHANGE_WORDS:
        for phrase1 in WAKE_WORDS:
            if phrase1 in text_in:
                text_in=text_in.replace(phrase1,'')
        if phrase in text_in:
            text=text_in.replace(phrase,'')
            response(exchangeRate.exchange(text))
            return

    for phrase in GOOGLE_SEARCH_WORDS:
        for phrase1 in WAKE_WORDS:
            if phrase1 in text_in:
                text_in=text_in.replace(phrase1,'')
        if phrase in text_in:
            text=text_in.replace(phrase,'')
            response("Avvio la ricerca, ecco il risultato: ")
            openLinks.googleSearch(text)
            return

    response(skills.notUnderstand())

if __name__=='__main__':
    try:
        main()
    except:
        print("C'è stato un errore.")
