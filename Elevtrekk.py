import random

antall = int(input('Hvor mange skal trekkes? '))
navn = ['ole', 'bolle', 'odd', 'frank', 'jens']

def trekk_tilfeldig(n):
    trekk = random.sample(navn, n)
    return trekk

utvalg = trekk_tilfeldig(antall)

for folk in utvalg:
    print(folk)
