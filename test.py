fruits = ["Banane", "Cerise", "Poire","Pomme", "Orange"]
fruits.append("Framboise")

"""
for f in fruits:
    print f
"""
"""
i = 0
while i < len(fruits):
    print fruits[i]
    i += 1
"""

import os
import time


def SayHello(name):
    if name:
        print("hello " + name)
    else:
        name = raw_input("vous n'avez pas saisi de nom, merci d'en saisir un: ")
        SayHello(name)

SayHello('titi')
time.sleep(2)
os.system('Calc.exe')

def main():
    SayHello("titi")
    time.sleep(2)
    os.system('Calc.exe')
