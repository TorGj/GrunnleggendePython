import PySimpleGUI as sg

# set the theme for the screen/window
sg.theme("DarkTanBlue")

# define layout
options = [[sg.Frame('Choose your Bread', [[sg.Radio('Whole Wheat', 'rd_bread', key='Whole Wheat')]],
                     border_width=1)],
           [sg.Frame('Choose your Toppings', [[sg.Checkbox('Pepperoni', key='Pepperoni')]], title_location='ne',
                     background_color='grey')],
           [sg.Frame('Choose your Sauces', [[sg.Checkbox('Onion', key='Onion Sauce')]], title_color='yellow',
                     border_width=3)],
           [sg.Button('Submit', font=('Times New Roman', 12))]]

choices = [[sg.Frame('Customise Your Pizza', layout=options)]]

items_chosen = [[sg.Text('You have Chosen')],
                [sg.Text("", size=(50, 3), key='options')]]

# Create layout with two columns using precreated frames
layout = [[sg.Column(choices, element_justification='c'), sg.Column(items_chosen, element_justification='c')]]

# Define Window
window = sg.Window("Column and Frame", layout)
# Read  values entered by user
event, values = window.read()
# access all the values and if selected add them to a string
strx = ""
for val in values:
    if window.find_element(val).get() == True:
        strx = strx + " " + val + ","

while True:
    event, values = window.read()  # Read  values entered by user
    if event == sg.WIN_CLOSED:  # If window is closed by user terminate While Loop
        break
    if event == 'Submit':  # If submit button is clicked display chosen values
        window['options'].update(strx)  # output the final string
# Close Window
window.close()