listemedkunder =[]
sant = True

while sant:
    navn = input('Navn')
    adr = input('Adresse')
    listemedkunder.append(navn)
    if navn == 'tor':
        break




def lagre(resultat):
    with open('Tor.txt', 'a') as f:
        f.writelines(str(resultat))
        f.write('\n')
    f.close()


lagre(listemedkunder)
