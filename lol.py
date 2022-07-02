import PySimpleGUI as sg
choice, _ = sg.Window('Continue?', [[sg.T('Do you want to continue?')], [sg.Yes(s=100), sg.No(s=100)]], disable_close=True).read(close=True)