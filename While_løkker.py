import time
import matplotlib.pyplot as plt

def foo():
    i = int(0)      # Her dikterer jeg at variablen i skal være en Int
    while i < 10:
        print(i)
        i = i + 1
        if i == 8:  #
            break




fortsett = True
while fortsett:
    print('Var innom løkke 2')
    fortsett = False

foo()


a = 'greit'
b = str('ok')
while a == 'greit' or b == 'ok':
    print(b, 'løkke 3')
    if b == 'ok':
        a = 'nei'
        b = 'nope'


navn = ['Marcus', 'Liam', 'Marius', 'Robin', 'Kevin', 'Johannes', 'Benjamin', 'William', 'Erik', 'Deimantas', 'Bendik', 'Haidas', 'Romandus']
print('Antall i IM2:', len(navn))
n = 0
while navn[n] != 'Romandus':
    print(navn[n], end=' ')
    n = n + 1

# poppe navn
while len(navn) > 2:
    print(navn)
    utpoppa = navn.pop(1)    # Kaster/sender listeinnhold ut av lista, og lager en ny liste med samme navn.
    print('utpoppa', utpoppa)

foo()

n = 1
T=[]
N =[]
gogo = True
while gogo:
    tic = time.perf_counter()
    n = n + 1
    if n == 100:
        break
    toc = time.perf_counter()
    T.append(toc-tic)
    N.append(n)

plt.ylim(0, 0.000001)  # Max "høyeste pris i datasettet" øre på yakse
plt.bar(N,T, color='green')
plt.yscale('linear')  # Defines log/linear scale
plt.xlabel('x-tingy')
plt.show()

