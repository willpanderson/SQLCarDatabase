from tkinter import *

import mysql.connector

connection = mysql.connector.connect(host='localhost',port='3306',database='rentals',user='root',password='Superglide2')
c = connection.cursor(prepared=True)
root = Tk()
root.title("Add New Vehicle")
root.geometry("500x600")
vin = Entry(root, width = 30)
vin.grid(row = 1, column = 1, padx=20)

description = Entry(root, width = 30)
description.grid(row = 2, column = 1)

year = Entry(root, width = 30)
year.grid(row = 3, column = 1)

type = Entry(root, width = 30)
type.grid(row = 4, column = 1)

category = Entry(root, width = 30)
category.grid(row = 5, column = 1)

hint = Label(root, text = "Type:(0:Basic,1:Luxury) Category(1:Compact,2:Medium,3:Large,4:SUV,5:Truck,6:Van)")
hint.grid(row = 0, column = 0, columnspan = 2)
vin_label = Label(root,text = "VIN")
vin_label.grid(row = 1,column = 0)
description_label = Label(root,text = "Description")
description_label.grid(row = 2,column = 0)
year_label = Label(root,text = "Year")
year_label.grid(row = 3,column = 0)
type_label = Label(root,text = "Type")
type_label.grid(row = 4,column = 0)
category_label = Label(root,text = "Category")
category_label.grid(row = 5,column = 0)

def submit():
    c.execute("insert into vehicle (VehicleID, Description, Year, Type, Category) values (?,?,?,?,?)",(vin.get(),description.get(),year.get(),type.get(),category.get(),))
    c.execute("Select vehicle.year from vehicle where vehicle.VehicleID = ?",(vin.get(),))
    years = c.fetchall()
    c.execute("Select vehicle.description from vehicle where vehicle.VehicleID = ?",(description.get(),))
    make = c.fetchall()
    c.execute("Select vehicle.VehicleID from vehicle where vehicle.VehicleID = ?",(description.get(),))
    vin_c = c.fetchall()
    test = ("A" + str(years) +" rental car has been added to CarRental2019")
    response_label = Label(root,text = test)
    response_label.grid(row = 7,column = 1)

submit_button = Button(root, text = "Add Rental Vehicle",command = submit)
submit_button.grid(row = 6,column = 0,columnspan=2)

root.mainloop() 
