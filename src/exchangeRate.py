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

        if("$" in words[0]):
            fromCurrency='USD'
            x=1
            n=str(words[0].replace("$",""))        
        else:
            match(words[1]):
                case 'euro':
                    fromCurrency='EUR'
                case 'dollari'|'dollaro':
                    fromCurrency='USD'
                case 'sterline'|'sterlina':
                    fromCurrency=''
                case 'yen':
                    fromCurrency='JPY'
                case 'franchi'|'franco':
                    fromCurrency='CHF'
            n=str(words[0])
        match(words[3-x]):
            case 'euro':
                toCurrency='EUR'
            case 'dollari'|'dollaro':
                toCurrency='USD'
            case 'sterline'|'sterlina':
                toCurrency=''
            case 'yen':
                toCurrency='JPY'
            case 'franchi'|'franco':
                toCurrency='CHF'

        url = "https://api.apilayer.com/exchangerates_data/convert?to="+toCurrency+"&from="+fromCurrency+"&amount="+n
        API_KEY=open('exchange_api.txt','r').read()
        payload = {}
        headers= {
        "apikey": API_KEY
        }
        response = requests.request("GET", url, headers=headers, data = payload).json()
        val = response['result']
        val=str(val).replace(".",",")
        return("Equivalgono a "+str(val)+" "+str(words[3-x]))
    except:
        return("C'è stato un errore nella conversione, riprova.")


