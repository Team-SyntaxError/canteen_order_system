import secrets
import string
from database.func import add_recipe,list_recipes,update_recipe_stock,update_recipe_price
import PySimpleGUI as sg
sg.theme("DarkGreen")
recipes={}
all = list_recipes()
for x in all:
    recipes[x.get("recipe")]={"stock":x.get("stock"),"price":x.get("price")}
plain_receipes=[]
lst=[]
def_space=15
print(recipes)
for x in recipes:
    plain_receipes.append(x)
    space=len(x)-def_space
    space=abs(space)
    lst.append([sg.Text(x),sg.Text(" "*space),sg.Text(recipes.get(x).get("stock"),key=f"-{x}_stock-"),sg.Text(" "*def_space),sg.InputText(size=(10), key=f"{x}_stock"),sg.Text(" "*def_space),sg.Text(recipes.get(x).get("price"),key=f"-{x}_price-"),sg.Text(" "*def_space),sg.InputText(size=(10), key=f"{x}_price")])

layout = [    
    [sg.Text('FC BVRIT ADMIN PANEL', text_color="Red",justification="5")],
    [sg.Text("Product\t\tQuantity\t\tNew Quantity\t\tPrice\t\tNew Price")]
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
        print(values)
        for x in plain_receipes:
            if values[f"{x}_stock"]!='' or values[f"{x}_price"]!='':
                if values[f"{x}_stock"]!='':
                    update_recipe_stock({x:values[x]})
                    window[f"-{x}-"].update(values[x])
        window["-update-"].update("Server updated successfully.")
