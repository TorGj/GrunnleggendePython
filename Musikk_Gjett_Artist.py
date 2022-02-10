from playsound import playsound

def ps():
    playsound('musikk/sail.mp3', block=False)

ps()

while True:
    stopp = input('Stopp?')
    if stopp =='y':
        break