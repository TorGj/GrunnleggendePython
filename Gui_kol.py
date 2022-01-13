import PySimpleGUI as sg

sg.theme("DarkTanBlue")

options = [[sg.Frame('Radiovalg', [[sg.Radio('R Valg 1', 'v1', key='Valgt 1'),
                                    sg.Radio('R Valg 2', 'v1', key='Valgt 2'),
                                    sg.Radio('R Valg 3', 'v1', key='Valgt 3'),
                                    sg.Radio('R Valg 4', 'v1', key='Valgt 4'),
                                    sg.Radio('R Valg 5', 'v1', key='Valgt 5')]],
                     border_width=1, background_color='green', font=('Times New Roman', 20))],
           [sg.Frame('Multivalg nr 1', [[sg.Checkbox('C valg 1', key='C Valgt 1'),
                                         sg.Checkbox('C valg 2', key='C Valgt 2'),
                                         sg.Checkbox('C valg 3', key='C Valgt 3'),
                                         sg.Checkbox('C valg 4', key='C Valgt 4'),
                                         sg.Checkbox('C valg 5', key='C Valgt 5')]],
                     title_location='ne', background_color='#000000', font=('Times New Roman', 20))],
           [sg.Frame('Multivalg nr 2', [[sg.Checkbox('C2 Valg 1', key='C2 Valgt 1'),
                                         sg.Checkbox('C2 Valg 2', key='C2 Valgt 2'),
                                         sg.Checkbox('C2 Valg 3', key='C2 Valgt 3'),
                                         sg.Checkbox('C2 Valg 4', key='C2 Valgt 4')]],
                     title_color='yellow', border_width=1, font=('Times New Roman', 20))],
           [sg.Button('Oppdater kolonne', font=('Times New Roman', 20))]]

resultat = [[sg.Frame('Dine valg:', [[sg.Text("", size=(50, 20), key='key_for_oppdater')]], border_width=1)]]


# ************** Rammer for Kolonne 1 og 2 ********************************
choices = [[sg.Frame('Overskrift Venstre', layout=options)]]

items_chosen = [[sg.Frame('Resultat av valg', layout=resultat)]]
# **************


# Her lages de to kolonnene                  Skilles av , her
layout = [[sg.Column(choices, element_justification='c'), sg.Column(items_chosen, element_justification='c')]]

# Define Window
window = sg.Window("Kolonner og rammer", layout)

event, values = window.read()

strx = ""
for verdi in values:
    if window.find_element(verdi).get() == True:
        strx = strx + " " + verdi + ","      # En tekststreng vil bygges opp med valgene som er gjort.

while True:
    event, values = window.read()  # Her legges valgene inn i en dict
    if event == sg.WIN_CLOSED:  # Lukking av vinduet stopper programmet (det skjer bare med sg.WIN_CLOSED)
        break
    if event == 'Oppdater kolonne':  # If submit button is clicked display chosen values
        window['key_for_oppdater'].update(strx)  # oppdaterer kolonne til høyre
        event = ''

# Close Window
window.close()