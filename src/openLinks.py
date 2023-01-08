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
        keyword=keyword.replace("riproduci su youtube","")
        keyword=keyword.replace(" ","+")
        url="https://www.youtube.com/results?search_query=" + keyword
        openLink(url)
        return
    except:
        print('Errore.')
        return


def rickRoll():
    openLink('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

