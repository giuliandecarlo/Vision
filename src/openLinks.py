import webbrowser
import urllib.request
import re

def openLink(url):
    webbrowser.open_new_tab(url)

def getUrlYt(search_keyword): #Search on yt and returns the first result
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    url="https://www.youtube.com/watch?v=" + video_ids[0]
    return url

def googleSearch(keyword):
    try:
        url="https://www.google.com/search?q="
        keyword=keyword.replace("cerca su google","")
        keyword=keyword.replace(" ","+")
        print("TEST:"+keyword)
        if(keyword=="" or keyword=="+"):
            openLink("https://www.google.com")
            return
        url=url + keyword
        openLink(url)
        return
    except:
        print("Errore.")
        return

def ytPlay(keyword):
    try:
        keyword=keyword.replace("riproduci su youtube","")
        keyword=keyword.replace(" ","+")
        openLink(getUrlYt(keyword))
        return
    except:
        print('Errore.')
        return

def ytSearch(keyword):
    try:
        url="https://www.youtube.com/results?search_query="
        keyword=keyword.replace("riproduci su youtube","")
        keyword=keyword.replace(" ","+")
        print("TEST:"+keyword)
        if(keyword=="" or keyword=="+"):
            openLink("https://www.youtube.com")
            return
        url=url + keyword
        openLink(url)
        return
    except:
        print('Errore.')
        return


def rickRoll():
    openLink('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
