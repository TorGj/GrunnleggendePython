def lagre(resultat, bruker, alt):
    with open('%s.txt' % bruker, '%s' % alt) as f:
        f.writelines(str(resultat))
        f.write('\n')
    f.close()           # Close file to allow other to access file


def les_fil(bruker):
    min_fil = open('%s.txt' % bruker, 'r')
    innhold = min_fil.read()
    min_fil.close()     # Close file to allow other to access file
    return innhold

tilfil = str(input('Skriv det som skal lagres:'))
lagre(tilfil,'Tor', 'w')

lestfil = les_fil('Tor')
print(lestfil)

