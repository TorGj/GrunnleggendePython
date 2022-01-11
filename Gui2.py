import PySimpleGUI as sg
# Dummycomment....
sg.theme('SandyBeach')

layout = [
	[sg.Text('Din info')],
	[sg.Text('Name', size=15), sg.InputText()],
	[sg.Text('Melding', size =15), sg.Multiline(size=(60, 5), key='textbox')],
	[sg.Submit("Send"), sg.Cancel("Avbryt")]]

window = sg.Window('Simple data entry window', layout)
event, values = window.read()
window.close()

# The input data looks like a simple list
# when automatic numbered
print(event, values[0], values[1], values[2])
