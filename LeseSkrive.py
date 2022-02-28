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