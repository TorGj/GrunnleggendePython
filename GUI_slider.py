import PySimpleGUI as sg
# En kommentar
layout = [
    [sg.Slider(range=(1,20), resolution=1, orientation='horizontal', enable_events=True, key='-NUM-')],
    [sg.Frame('Frame', [[sg.Text("a big number".ljust(30), key='-TEXT-')]])]
]

window = sg.Window("Title", layout)

while True:
    event, values = window.read()
    print(event, values)

    if event == sg.WINDOW_CLOSED:
        break

    if event == '-NUM-':
        number = str(10**int(values['-NUM-']))
        window['-TEXT-'].update(number.ljust(30))

window.close()