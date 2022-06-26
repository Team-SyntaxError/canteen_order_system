import secrets
import string
from database.func import add,list_recipes
import PySimpleGUI as sg
import qrcode  
from PIL import Image
def passgen():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(60))
    password = password.replace("'", '"')
    return password.replace('"',"*")
sg.theme("DarkGreen")
recipes={}
all = list_recipes()
for x in all:
    recipes[x.get("recipe")]=x.get("stock")
lst=[]
def_space=15
plain_receipes=[]
for x in recipes:
    plain_receipes.append(x)
    space=len(x)-def_space
    space=abs(space)
    lst.append([sg.Text(x),sg.Text(" "*def_space),sg.Text(recipes.get(x)),sg.Text(" "*def_space),sg.InputText(size=(10), key=x,default_text="0")])


layout = [
    [sg.Text('FC BVRIT', text_color="Red",justification="5")],
    [sg.Text("Product\t\tQuantity Avaiable\t\tQuantity Ordering")]
]
for x in lst:
    layout.append(x)
layout.append([sg.Button('BILL IT')])
layout.append([sg.Button('ANALYSE BILL')])
layout.append([sg.Text(key='-bill-', text_color="Red")])
layout.append([sg.Text('TOTAL: ', text_color="Red"), sg.Input("", key='-ORDER-')])
layout.append([sg.Button('ORDER')])
layout.append([sg.Cancel()])
window = sg.Window('FC ORDER SYSTEM', layout,icon=r'C:\Users\chsai\Desktop\folder_locker\enc.ico', size=(600, 400))
# add(dic,password)
while True:
    event, values = window.read()
    if event is None or event == 'Cancel':
        break
    if event=="BILL IT":
        vle=0
        for x in plain_receipes:
            if int(values[x])!=0:
                vle+=int(values[x])
        window['-ORDER-'].update(vle)
    if event=="ANALYSE BILL":
        vle=0
        for x in plain_receipes:
            if int(values[x])!=0:
                vle+=int(values[x])
        if vle==0:
            window["-bill-"].update("NOTHING TO ANALYSE, CART IS EMPTY.")
        else:
            txet="BILL ANALYSIS\nPRODUCT NAME\t\tRATE\t\tQUANTITY\t\tPRICE"
            for x in plain_receipes:
                if int(values[x])!=0:
                    txet+=f'\n{x.upper()}\t\t\t130\t\t{int(values[x])}\t\t\t{int(values[x])*130}'
            
            window["-bill-"].update(txet)
    if event=="ORDER":
        lst={}
        for x in plain_receipes: 
            if int(values[x])!=0:
                lst[x]=int(values[x])
        key = passgen()
        add(lst,passgen())
        order = {"key":key, "dict":lst}
        qr_img = qrcode.make(str(order))
        qr_img.save("qr-img.jpg")
        im = Image.open(r"qr-img.jpg")
        im.show()


                

