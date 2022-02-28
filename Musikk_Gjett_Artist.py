from pygame import mixer
import os, random

poeng = 0

def velg_artist():
    valg = random.choice(os.listdir("musikk"))
    while valg.startswith("."):
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

def formater(line):
    n = 3 #ant. tegn som må være riktige
    return [line[i:i + n] for i in range(0, 3, n)]


while True:
    valgt = velg_artist()
    fasit = formater(valgt[0])
    # print(valgt)

    ps(valgt[0])

    stopp = input('Hvem er dette?')
    svar = formater(stopp)

    print(valgt[0])

    if fasit[0].lower() == svar[0].lower():
        poeng = poeng + 1
        print('Du har ', poeng, ' poeng')

    if poeng > 5:
        print('Vi har en vinner ... DU vant')
        break

