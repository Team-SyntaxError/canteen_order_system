import secrets
import string
from database.func import add
import PySimpleGUI as sg

def passgen():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(60))
sg.theme("DarkGreen")
layout = [
    [sg.Text('FC BVRIT', text_color="Red")],
    [sg.Checkbox('PIZZA', default=False, key="PIZZA"),sg.Input(size=(10), key="pizza") ],
    [sg.Button('BILL IT')],
    [sg.Text('TOTAL: ', text_color="Red"), sg.Input("", key='-FINAL-')],

    [sg.Cancel()],
]
window = sg.Window('FC ORDER SYSTEM', layout,icon=r'C:\Users\chsai\Desktop\folder_locker\enc.ico', size=(500, 500))
# add(dic,password)
while True:
    event, values = window.read()
    if event is None or event == 'Cancel':
        break
    if values["-OUTPUT-"]:
        window['-FINAL-'].update(values["pizza"]*130)
