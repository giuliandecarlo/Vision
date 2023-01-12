import requests


def exchange(text):
    try:
        print(text)
        x=0
        n=""
        toCurrency=""
        fromCurrency=""
        words=text.split()
        if(words[0]=='un' or words[0]=='uno'):
            n='1'

        if("€" in words[0]):
            fromCurrency='EUR'
            x=1
            n=str(words[0].replace("€",""))
        elif("$" in words[0]):
            fromCurrency='USD'
            x=1
            n=str(words[0].replace("$",""))        
        else:
            fromCurrency=codeCurrency(words[1])
            n=str(words[0])
            toCurrency=codeCurrency(words[3-x])

        url = "https://api.apilayer.com/exchangerates_data/convert?to="+toCurrency+"&from="+fromCurrency+"&amount="+n
        API_KEY=open('exchange_api.txt','r').read()
        payload = {}
        headers= {
        "apikey": API_KEY
        }
        response = requests.request("GET", url, headers=headers, data = payload).json()
        val = response['result']
        val=round(val,2)
        val=str(val).replace(".",",")
        return("Equivalgono a circa "+str(val)+" "+str(words[3-x]))
    except:
        return("C'è stato un errore nella conversione, riprova.")

def codeCurrency(text):
       match(text):
            case 'euro':
                return 'EUR'
            case 'dollari'|'dollaro':
                return 'USD'
            case 'sterline'|'sterlina':
                return 'GBP'
            case 'yen':
                return 'JPY'
            case 'franchi'|'franco':
                return 'CHF'
            case _:
                return ''


