import secrets
import string
from database.func import add,list_recipes,key_info,update_recipe_stock
import PySimpleGUI as sg
import qrcode  
from PIL import Image
from tinydb import TinyDB, Query
db = TinyDB('db.json')
def passgen():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(60))
    password = password.replace("'", '"')
    return password.replace('"',"*")
sg.theme("DarkTeal10")
font = ("Helvetica", 13)
sg.set_options(font=font)
recipes={}
all = list_recipes()
for x in all:
    recipes[x.get("recipe")]={"stock":x.get("stock"),"price":x.get("price"), "is_special":x.get("is_special")}
# print(recipes)
lst=[]
lst_spcl=[]
def_space=15
plain_receipes=[]
for x in recipes:
    plain_receipes.append(x)
    space=len(x)-def_space
    space=abs(space)
    if recipes.get(x).get("is_special")==True:
        nme=x.ljust(24," ")
        nme1=recipes.get(x).get("price").strip().ljust(28," ")
        nme2=recipes.get(x).get("stock").strip().ljust(35," ")
        lol = nme+nme1+nme2
        lst_spcl.append([sg.Text(lol,text_color="white"),sg.InputText(size=(10), key=x,)])
    else:
        nme=x.ljust(24," ")
        nme1=recipes.get(x).get("price").strip().ljust(28," ")
        nme2=recipes.get(x).get("stock").strip().ljust(35," ")
        lol = nme+nme1+nme2
        lst.append([sg.Text(lol,text_color="white"),sg.InputText(size=(10), key=x,)])

layout = [
    [sg.Text('FOOD COURT', text_color="cyan",justification="5")],
    [sg.Text('Regular Items',text_color="pink")],
    [sg.Text("Product\t\tPrice\t\tQuantity Avaiable\t\tQuantity Ordering", text_color="yellow")]
]

for x in lst:
    layout.append(x)
layout.append([sg.Text('Special Items', text_color="pink")])
layout.append([sg.Text("Product\t\tPrice\t\tQuantity Avaiable\t\tQuantity Ordering", text_color="yellow")])
for x in lst_spcl:
    layout.append(x)
layout.append([sg.Button('BILL IT',button_color="green")])
layout.append([sg.Button('ANALYSE BILL', button_color="green")])
layout.append([sg.Text(key='-bill-', text_color="yellow")])
layout.append([sg.Text('TOTAL: ', text_color="yellow"), sg.Input("", key='-ORDER-')])
layout.append([sg.Checkbox('take away?', default=False,key="is_parcel")])
layout.append([sg.Button('ORDER',button_color="green")])
layout.append([sg.Text(key='-ttt-', text_color="white")])
layout.append([sg.Button('My Orders')])
layout.append([sg.Cancel(button_color="green")])
window = sg.Window('CANTEEN ORDER SYSTEM', layout,icon=r'C:\Users\chsai\Desktop\folder_locker\enc.ico', size=(1000, 900))
while True:
    event, values = window.read()
    if event is None or event == 'Cancel':
        break
    if event=="My Orders":
        my_order="Your Order List is: \n"
        num=1
        for item in db:
            p = key_info(item.get("key"))
            if p:
                if num<1:
                    my_order+=f"Order Number: {num}\n"
                else:
                    my_order+=f"\n\nOrder Number: {num}\n"
                num+=1
                for x in p.get("dict"):
                    my_order+=f"{x}     {p.get('dict').get(x)}\n"
                my_order+=f"Key:  {p.get('key')}"
        sg.popup_scrolled(my_order)
    if event=="BILL IT":
        vle=0
        for x in plain_receipes:
            if (values[x])!='':
                vle+=int(values[x])*int(recipes.get(x).get("price"))
        window['-ORDER-'].update(vle)
    if event=="ANALYSE BILL":
        vle=0
        for x in plain_receipes:
            if (values[x])!='':
                vle+=int(values[x])
        if vle==0:
            window["-bill-"].update("NOTHING TO ANALYSE, CART IS EMPTY.")
        else:
            txet="BILL ANALYSIS\nPRODUCT NAME\t\tRATE\t\tQUANTITY\t\tPRICE"
            for x in plain_receipes:
                if (values[x])!='':
                    txet+=f'\n{x.upper()}\t\t\t{int(recipes.get(x).get("price"))}\t\t{int(values[x])}\t\t\t{int(values[x])*int(recipes.get(x).get("price"))}'
            
            window["-bill-"].update(txet)
    if event=="ORDER":
        overflow=False
        lst={}
        stock_update={}
        for x in plain_receipes: 
            if (values[x])!='':
                if int(values[x])>int(recipes.get(x).get("stock")):
                    window["-ttt-"].update(f"{x}'s entered stock is more than avaiable")
                    overflow=True
                    break
                else:
                    lst[x]=int(values[x])
                    stock_update[x]=int(recipes.get(x).get("stock"))-int(values[x])
                    overflow=False
        if not overflow:
            key = passgen()
            if len(lst) == 0:
                window["-ttt-"].update("Cart is empty")
            else:
                window["-ttt-"].update("Cart is empty")
                add(lst,key,values['is_parcel'])
                order = {"key":key, "dict":lst, "is_parcel":str(values['is_parcel'])}
                db.insert({"key":key})
                # print(order)
                print(stock_update)
                update_recipe_stock(stock_update)
                qr_img = qrcode.make(str(order))
                qr_img.save("qr-img.jpg")
                im = Image.open(r"qr-img.jpg")
                im.show()


                

