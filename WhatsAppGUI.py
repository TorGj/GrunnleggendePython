import PySimpleGUI as psg
# sass...
def GUI():
    psg.theme('TealMono')
    #definer layout
    layoutA=[[psg.Text('Send til nr', size=10, font='Lucida', justification='left'), psg.InputText(size=10)],
             [psg.Text('Melding:', size=10, font='Lucida', justification='left'), psg.Multiline(size=(60, 6), key='textbox')],
             [psg.Radio('Send nå', 'naa', font='Lucida', key='send_naa'), psg.Radio('Velg tid', 'naa', font='Lucida', key='send_senere')],
             [psg.Text('', size=10, font='Lucida', justification='left'), psg.InputText(size=5), psg.InputText(size=5)],
             [psg.Button('Send Melding', font=('Times New Roman', 14)), psg.Button('Glem det', font=('Times New Roman', 14))]]
    #Definer Window
    window = psg.Window('Send WhatsApp-melding', layoutA)
    e, v = window.read()
    print(e, v)
    window.close()

    svar = list(v.values())
    return svar
