navn = ['Tor', 'Ole', 'Ola', 'Per', 'Odd', 'Jan', 'Tom', 'Are',
        'Ian', 'Jon', 'Ove', 'Roy', 'Åge', 'Ali', 'Don', 'Ron',
        'Liv', 'Ann', 'Gry', 'Oda', 'Sia', 'Lea', 'Lan',
        'Eli', 'Eva', 'Mia', 'Ine', 'Fia', '']

print('Lengde på lista:', len(navn))

for ele in navn:
    print(ele, end=' ')





print('') # ny linje ... ny for løkke

for i in range(len(navn)):
    print(navn[i], end='_')

print('')






for i in range(3, 13, 2):
    print(navn[i], end='.')





def summere_verdi_av_elementer_i_liste():
    print('')  # Lager ny linje ..... her er ny For-løkke
    tall = [6, 5, 3, 8, 4, 2, 5, 4, 11]
    sum = 0

    for verdi in tall:
        sum = sum + verdi
    print("Summen er: ", sum)

#while True:
    summere_verdi_av_elementer_i_liste()
summere_verdi_av_elementer_i_liste()
