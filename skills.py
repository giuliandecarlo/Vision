import datetime


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