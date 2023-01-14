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
        
    if(minute==0):
        return text_out
    else:
        text_out=text_out+" e "+str(minute)+" minuti "
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