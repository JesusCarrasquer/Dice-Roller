import platform
import os

def getCurrentOS():
    return platform.system()

def stopProgram():
    quit(0)
def clearConsole():
    if getCurrentOS() == 'Windows':
        os.system('cls')
    elif getCurrentOS() == 'Linux':
        os.system('clear')

def listSaved():
    return os.listdir('./Memory')