from playsound import playsound
from pygame import mixer
import time
import os, random

poeng = 0

def velg_artist():
    valg = random.choice(os.listdir("musikk"))
    while valg == '.DS_Store':
        valg = random.choice(os.listdir("musikk"))
    artist = valg.split("_")
    artist = artist[0]
    #print(valg)
    return valg, artist

def ps(sang):
    mixer.init()  # Initialzing pyamge mixer
    mixer.music.stop()
    mixer.music.load('musikk/%s' %sang)  # Loading Music File
    mixer.music.play()  # Playing Music with Pygame
    #time.sleep(5)
    #print('musikk/%s' % sang)

while True:
    valgt = velg_artist()
    print(valgt)
    ps(valgt[0])
    stopp = input('Hvem er dette?')

    print(valgt[1])
    if stopp == valgt[1]:
        poeng = poeng + 1

    if poeng > 2:
        break

