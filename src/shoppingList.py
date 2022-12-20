def getList():
    f=open('list.txt')
    data=f.read()
    f.close()
    if(len(data.strip())==0):
        return("La lista della spesa è vuota.")
    else:
        return("La lista della spesa contiene: "+data)

def removeList(text):
    notInList=True
    try:
        print(text)
        if("dalla lista della spesa" in text):
            text=text.replace("dalla lista della spesa",'')
            element=text.replace("rimuovi",'')
        else:
            return("c'è stato un errore, riprova.")
        print(element)
        with open("list.txt","r") as inFile:
            lines=inFile.readlines()
        with open("list.txt","w+") as inFile:
            for line in lines:
                if line.strip()!=element.strip() and line.strip():  
                    inFile.write(line)
                else:
                    notInList=False
        if(notInList):
            return("L'elemento che hai detto non è presente nella lista della spesa.")
        else:
            return("Elemento rimosso correttamente dalla lista della spesa.")
    except:
        return("c'è stato un errore, riprova.")
            
def removeAll():
    open('list.txt', 'w').close()
    return("La lista della spesa è stata svuotata correttamente.")
        
def addList(text):
    if("alla lista della spesa" in text):
        text=text.replace("alla lista della spesa",'')
        element=text.replace("Aggiungi",'')
    else:
        return("c'è stato un errore, riprova.")
    try:
        file=open("list.txt")
        while True:
            line=file.readline()
            if not line:
                file.close()
                break
            if(line==element or line==element+"\n"):
                file.close()
                return("L'elemento scelto è già presente nella lista della spesa.")   
        with open("list.txt","a+") as f:
            f.write("\n"+str(element))
            f.close()
            return(element+" è stato aggiunto alla lista della spesa.")
    except:
        return("c'è stato un errore, riprova.")

