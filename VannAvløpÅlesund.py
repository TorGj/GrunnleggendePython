
forbruk = float(input('Forbuk i m3 (vanlig: 150 - 200)'))
fast_aarspris = float(903)
vann = float(19.09)
avlop = float(26.51)

avslutte = input('Avslutte?')
print(avslutte)
print(avslutte.lower())
while avslutte.lower() == 'y':
    print('slutt')


totalt = fast_aarspris + forbruk * (vann + avlop)
print('Totalt for året:', totalt)
print('Pris pr liter kaldt vann:', round((totalt*100)/(forbruk*1000),2), 'øre')
print('Pris pr liter varmt vann: 4.5 øre i tillegg')
print('Badekar 1 gang:', 300*(0.05+0.045),'kr')


