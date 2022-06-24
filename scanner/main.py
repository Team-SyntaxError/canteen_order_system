import secrets
import string
from database.func import add
import PySimpleGUI as sg
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import json

def decoder(image):
    gray_img = cv2.cvtColor(image,0)
    barcode = decode(gray_img)

    for obj in barcode:
        points = obj.polygon
        (x,y,w,h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

        barcodeData = obj.data.decode("utf-8")
        barcodeType = obj.type
        return barcodeData
        
sg.theme("DarkGreen")
layout = [
    [sg.Text('FC QR SCANNER', text_color="Red")],
    [sg.Button('SCAN QR')],
    [sg.Text(key='-TXT-', text_color="Red")],
    [sg.Cancel()],
]
window = sg.Window('FC ORDER SYSTEM', layout,icon=r'C:\Users\chsai\Desktop\folder_locker\enc.ico', size=(500, 500))
# add(dic,password)
while True:
    event, values = window.read()
    if event is None or event == 'Cancel':
        break
    if values["SCAN QR"]:
      cap = cv2.VideoCapture(0)
      while True:
          ret, frame = cap.read()
          orders=decoder(frame)
          break
    ordlst = json.loads(orders)
    bill="FC BIll"
      for x in ordlst["orders"]:
            bill+=f"\n{x} {ordlst["orders"][x]}"
      window['-TXT-'].update("Select file or folder")
