import datetime as dt
import time
import random

navn = input('Hvem er du?')

ordliste =['hest', 'vanlig', 'kanin', 'friminutt', 'ferie', 'is', 'sol']

# kommandoen CHOICES returnerer en liste, selv om antall elementer er ett.
# For å trekke ut kun innholdet står det at variablen skal hente ut element 0
v_ord = random.choices(ordliste, k=1)[0]

a = time.perf_counter()
b_ord = input('Skriv: {}  :'.format(v_ord))
t_ord = time.perf_counter() - a

def test(p, u, s, t):
    if p == s:
        print('God rettskiving, du brukte:', round(t, 2), 'sekunder.')
        korrekt = []
        korrekt.append(u)
        korrekt.append(p)
        korrekt.append(t_ord)
        return korrekt
    else:
        print('stavefeil')


def lagre(resultat, bruker):
    with open('%s.txt' % bruker, 'w') as f:
        f.writelines(str(resultat))
        f.write('\n')
    f.close()           # Close file to allow other to access file

def les_fil(bruker):
    min_fil = open('%s.txt' % bruker, 'r')
    innhold = min_fil.read()
    min_fil.close()     # Close file to allow other to access file
    return innhold


def vis_stats(bruker, ord):
    print('Tidligere resultater for:', ord)
    innhold = les_fil(bruker)

    print(innhold)


res_ultat = test(v_ord, navn, b_ord, t_ord)
vis_stats(navn, v_ord)

lagre(res_ultat, navn)