i = 0
while i < 10:
    print(i)
    i = i + 1
    if i == 8:
        break


fortsett = True
while fortsett:
    print('Var innom løkke 2')
    fortsett = False


a = 'greit'
b = 'ok'
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

