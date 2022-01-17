import PySimpleGUI as sg

sg.theme("DarkTanBlue")


# *********************** Innholdet i Kolonnene  ... 3 kolonner ************************
kolonne_1 = [[sg.Text('Kolonne A1 R1 1'), sg.Text('Kolonne A1 R1 2')],
            [sg.Text('Kolonne A1 R2 1'), sg.Text('Kolonne A1 R2 2')] ]

kolonne_2 = [[sg.Text('Kolonne B1 1'), sg.Text('Kolonne B1 2')] ]

kolonne_3 = [[sg.Text('Kolonne C1 1')], [sg.Text('Kolonne C1 2')] ]
# **************************************************************************************


# ~~~~~~~~~~~~~~~~~~~~~~~~~ Rammene rundt kolonnene ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ramme_kol_1 = [[sg.Frame('Overskrift Kolonne 1', layout=kolonne_1, size=(400, 100))]]
ramme_kol_3 = [[sg.Frame('Overskrift Kolonne 3', layout=kolonne_3, size=(400, 100))]]
bunn_ramme = [[sg.Text('Bunnramme c1r1'), sg.Text('c1r2')]]
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ———————————————————————  Legg merke til den i midten  (har ikke ramme) ——————————————
hele_greia = [[sg.Column(ramme_kol_1), sg.Column(kolonne_2), sg.Column(ramme_kol_3)],
              [sg.Frame('Ramme i bunn', layout=bunn_ramme, key='bunnframe', size=(1110, 200))]]
# —————————————————————————————————————————————————————————————————————————————————————


# xxxxxxxxxxxxxxxxxxxxxxxx Definisjonen av vinduet og genskaper for alt inni xxxxxxxxxxx
window = sg.Window("Kolonner og rammer", hele_greia, font=('Arial', 20))
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


# ************** Leser ut verdier, pr nå så er det ingenting som kan velges ************
event, values = window.read()
# **************************************************************************************


window.close()