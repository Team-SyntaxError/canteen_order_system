import secrets
import string
from database.func import add_recipe,list_recipes,update_recipe
import PySimpleGUI as sg
sg.theme("DarkGreen")
recipes={}
all = list_recipes()
for x in all:
    recipes[x.get("recipe")]=x.get("stock")
plain_receipes=[]
lst=[]
def_space=15
for x in recipes:
    plain_receipes.append(x)
    space=len(x)-def_space
    space=abs(space)
    lst.append([sg.Text(x),sg.Text(" "*space),sg.Text(recipes.get(x),key=f"-{x}-"),sg.Text(" "*def_space),sg.InputText(size=(10), key=x)])

layout = [    
    [sg.Text('FC BVRIT ADMIN PANEL', text_color="Red",justification="5")],
    [sg.Text("Product\t\tQuantity\t\tNew Quantity")]
]
for x in lst:
    layout.append(x)
layout.append([sg.Button('UPDATE STOCK')])
layout.append([sg.Text(key='-update-', text_color="Red")])
layout.append([sg.Cancel()])
window = sg.Window('FC ORDER SYSTEM', layout,icon=r'C:\Users\chsai\Desktop\folder_locker\enc.ico', size=(600, 400))
while True:
    event, values = window.read()
    if event is None or event == 'Cancel':
        break
    if event=="UPDATE STOCK":
        for x in plain_receipes:
            if values[x]!='':
                    update_recipe({x:values[x]})
                    window[f"-{x}-"].update(values[x])
        window["-update-"].update("Server updated successfully.")
