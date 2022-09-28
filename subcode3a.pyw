from tkinter import *

import mysql.connector

connection = mysql.connector.connect(host='localhost',port='3306',database='rentals',user='root',password='Superglide2')
c = connection.cursor(prepared=True)
root = Tk()
root.title("Search Available Cars to Rent")
root.geometry("500x700")

hint = Label(root, text = "Type:(0:Basic,1:Luxury) Category(1:Compact,2:Medium,3:Large,4:SUV,5:Truck,6:Van)")
hint.grid(row = 0, column = 0, columnspan = 2)

category = Entry(root,width=30)
category.grid(row = 1, column = 1)
vtype = Entry(root,width=30)
vtype.grid(row = 2, column = 1)

cat_label = Label(root, text = "Vehicle Type")
cat_label.grid(row = 1, column = 0)
vtype_label = Label(root, text = "Vehicle Category")
vtype_label.grid(row = 2, column = 0)

format = Label(root, text = "VIN Description Year Type Category")
format.grid(row = 4, column = 0, columnspan = 2)

def submit():
    c.execute("select vehicle.VehicleID, vehicle.Description, vehicle.Year, vehicle.Type, vehicle.Category FROM Vehicle WHERE vehicle.Type = ? and vehicle.Category = ? and vehicle.VehicleID NOT IN (SELECT rental.VehicleID FROM rental)",(vtype.get(),category.get(),))
    print_records = ''
    labelList = [None] * 1000
    print_records = c.fetchall()
    for x,item in enumerate(print_records):
        labelList[x] = Label(root, text = item)
        labelList[x].grid(row = 5 + x, column = 0, columnspan = 2)

submit_button = Button(root, text = "Search For Vehicles",command = submit)
submit_button.grid(row = 3,column = 0,columnspan=2)

root.mainloop() 