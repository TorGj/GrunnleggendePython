import pywhatkit
import WhatsAppGUI
import datetime as dt
# Spør bruker om melding
# Til hvem.
# Sett inn datetime "nå" +1 min
# Gjør om til int og bruk variablen i msg..
# pySimpleGUI?
v = WhatsAppGUI.GUI()

if str(v[2]) == 'True':
    t = int(dt.datetime.today().strftime("%-H"))
    m = int(dt.datetime.today().strftime("%-M"))+1
else:
    t = int(str(v[3]))
    m = int(str(v[4]))

nr = '+47'+str(v[0])
mld = str(v[1])
print(nr, mld, t, m)

pywhatkit.sendwhatmsg(nr, mld, t, m)



