import secrets
import string
from database.func import add_recipe,list_recipes,update_recipe_stock,update_recipe_price,remove_recipe,is_recipe,get_tokens
import PySimpleGUI as sg
sg.theme("DarkGreen")
font = ("Helvetica", 13)
sg.set_options(font=font)
recipes={}
all = list_recipes()
for x in all:
    recipes[x.get("recipe")]={"stock":x.get("stock"),"price":x.get("price")}
tokens=get_tokens()
plain_receipes=[]
lst=[]
for x in recipes:
    plain_receipes.append(x)
    nme=x.ljust(24," ")
    nme1=recipes.get(x).get("price").strip().ljust(22," ")
    nme2=recipes.get(x).get("stock").strip().ljust(24," ")
    nme3="".ljust(17," ")
    lst.append([sg.Text(nme),sg.Text(nme2,key=f"-{x}_stock-"),sg.InputText("",size=(10), key=f"{x}_stock"),sg.Text(nme3),sg.Text(nme1,key=f"-{x}_price-"),sg.InputText(size=(10), key=f"{x}_price")])

layout = [    
    [sg.Text('CANTEEN ADMIN PANEL', text_color="Red",justification="5")],
    [sg.Text("Product\t\tQuantity\t\tNew Quantity\t\tPrice\t\tNew Price")]
]
for x in lst:
    layout.append(x)
layout.append([sg.Button('UPDATE STOCK')])
layout.append([sg.Text(key='-update-', text_color="Red")])
layout.append([sg.Text('Add/Remove Products', text_color="Red")])
layout.append([sg.Text("Product\t\t\tQuantity\t\t\tPrice")])
layout.append([sg.InputText(size=(10),key="prod_name"),sg.Text("\t"),sg.InputText(size=(10),key="prod_quan"),sg.Text("\t"),sg.InputText(size=(10),key="prod_price"),sg.Checkbox('is special?', default=False,key="is_special")])
layout.append([sg.Button('Add Product'),sg.Text("  "),sg.Button('Remove Product')])
layout.append([sg.Text(key='-msggg-', text_color="Red")])
layout.append([sg.Button('View Orders')])
layout.append([sg.Cancel()])
window = sg.Window('CANTEEN ORDER SYSTEM', layout,icon=r'C:\Users\chsai\Desktop\folder_locker\enc.ico', size=(1000, 700))
while True:
    event, values = window.read()
    if event is None or event == 'Cancel':
        break
    if event=="View Orders":
        tokens=get_tokens()
        l=0
        for z in tokens:
            l+=1
        my_order=f"Pending Orders Count: {l}\n"
        my_order+="Users Order List is: \n"
        num=1
        tokens=get_tokens()
        for x in tokens:
            my_order+=f"\n\nOrder Number: {num}\n"
            my_order+=f"key: {x.get('key')}\n"
            for y in x.get("dict"):
                my_order+=f"{y}     {x.get('dict').get(y)}\n"
            num+=1
        sg.popup_scrolled(my_order)
    if event=="Add Product":
        print(values)
        if values['prod_quan'].isdigit() ==False or values['prod_price'].isdigit() ==False:
            window[f"-msggg-"].update("Quantity and price should be a number")
        else:
            if values['prod_name'].capitalize() in plain_receipes:
                window[f"-msggg-"].update("Product with same name already exists")
            else:
                add_recipe(values['prod_name'].capitalize(), values['prod_quan'], values['prod_price'],values['is_special'])
                plain_receipes.append(values['prod_name'].capitalize())
                window[f"-msggg-"].update("Product added successfully")
    if event=="Remove Product":
        if is_recipe(values['prod_name'].capitalize()):
            remove_recipe(values['prod_name'].capitalize())
            plain_receipes.remove(values['prod_name'].capitalize())
            window[f"-msggg-"].update("Product Removed successfully")
        else:
            window[f"-msggg-"].update("No such product exists")
    if event=="UPDATE STOCK":
        print(values)
        for x in plain_receipes:
            if values[f"{x}_stock"]!='' or values[f"{x}_price"]!='':
                if values[f"{x}_stock"]!='':
                    if values[f"{x}_stock"].isdigit() ==False:
                        window[f"-update-"].update("Quantity and price should be a number")
                    else:
                        
                        nme2=values.get(f"{x}_stock").ljust(24," ")
                        update_recipe_stock({x:values.get(f"{x}_stock")})
                        window[f"-{x}_stock-"].update(nme2)
                        window["-update-"].update("Server updated successfully.")
                if values[f"{x}_price"]!='':
                    if values[f"{x}_price"].isdigit() ==False:
                        window[f"-update-"].update("Quantity and price should be a number")
                    else:
                        nme1=values.get(f"{x}_price").ljust(22," ")
                        update_recipe_price({x:values.get(f"{x}_price")})
                        window[f"-{x}_price-"].update(nme1)
                        window["-update-"].update("Server updated successfully.")