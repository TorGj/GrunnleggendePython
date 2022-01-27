navn = ['Tor', 'Ole', 'Ola', 'Per', 'Odd', 'Jan', 'Tom', 'Are',
        'Ian', 'Jon', 'Ove', 'Roy', 'Åge', 'Ali', 'Don', 'Ron',
        'Liv', 'Ann', 'Gry', 'Oda', 'Sia', 'Lea', 'Lan',
        'Eli', 'Eva', 'Mia', 'Ine', 'Fia', '']

print(len(navn))

for ele in navn:
    print(ele, end=' ')

print('') # ny linje

for i in range(len(navn)):
    print(navn[i], end='_')



