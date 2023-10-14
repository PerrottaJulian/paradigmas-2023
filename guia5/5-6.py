"""
Diseñar una rutina que imprima el cartel:
PRESIONE ENTER
PARA CONTINUAR
"""
import time

def printAnimation(string):
    for letra in string:
        print(letra, end="")
        time.sleep(0.1)

cartel = "PRESIONE ENTER\nPARA CONTINUAR"

printAnimation(cartel)