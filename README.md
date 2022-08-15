# Canteen Food Order System

It is a simple Python GUI built with PySimpleGui and MongoDB backend.

## Prerequisites
- Python 3

## Usage
- Clone the repository :
 ```
$ git clone https://github.com/chsaiujwal/canteen_order_system.git
``` 
- Install Dependencies :
```
$ pip install -r requirements.txt
```
- Edit the config.py and add your MongoDB URL.
- Navigate to admin or client or scanner folder and run `python3 main.py`

## How to use it?
The repo comprises of 3 folders, they are client, scanner and admin.

- ### client
    Customers can use the client application to place new orders, view already ordered orders. Once the order is placed, A QR Code is generated. Customer needs to scan this QR Code with the Canteen's Scanner to get food and final receipt. 

- ### admin
    The Canteen manager can use this portal to add/remove receipes, update receipes price/quantity, view ordes.
- ### scanner
    This scanner is placed in canteen. It scans the QR codes and gives order bill.

## Features
- It uses token based authentication, so fake QR Codes are identified. 
- The admin has a option to tag any item as special, so its diaplayed under "special items" category for customer.
- The customer has a option to tag a order as take away.
