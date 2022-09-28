from tkinter import *

import mysql.connector

connection = mysql.connector.connect(host='localhost',port='3306',database='rentals',user='root',password='Superglide2')
c = connection.cursor(prepared=True)


root = Tk()
root.title("Vehicle Lookup")
root.geometry("400x600")
Vin = Entry(root, width = 30)
Vin.grid(row = 1, column = 1, padx=20)
Description = Entry(root, width = 30)
Description.grid(row = 2, column = 1, padx=20)
vin_label = Label(root,text = "Vin")
vin_label.grid(row = 1,column = 0)
description_label = Label(root,text = "Description")
description_label.grid(row = 2,column = 0)

def submit_lookup():
    if (Vin.get() == ""):
        vlists = '%' + Description.get() + '%'

        c.execute("SELECT vRentalInfo.VIN, vRentalInfo.Vehicle, Avg(RATE.Daily) FROM RATE, vRentalInfo, VEHICLE WHERE vRentalInfo.Vehicle LIKE ? AND RATE.Type = VEHICLE.Type AND RATE.Category = VEHICLE.Category AND VEHICLE.VehicleID = vRentalInfo.VIN",(vlists,))
      
    elif (Description.get() == ""):
        dlists = '%' + Vin.get() + '%'

        c.execute("SELECT vRentalInfo.VIN, vRentalInfo.Vehicle, Avg(RATE.Daily) FROM RATE, vRentalInfo, VEHICLE WHERE vRentalInfo.VIN LIKE ? AND RATE.Type = VEHICLE.Type AND RATE.Category = VEHICLE.Category AND VEHICLE.VehicleID = vRentalInfo.VIN",(dlists,))
    elif (Vin.get() == "" and Description.get() == ""):

        c.execute("SELECT vRentalInfo.VIN, vRentalInfo.Vehicle, Avg(RATE.Daily) FROM RATE, vRentalInfo, VEHICLE WHERE RATE.Type = VEHICLE.Type AND RATE.Category = VEHICLE.Category AND VEHICLE.VehicleID = vRentalInfo.VIN ORDER BY RATE.Daily;")
    else:
        vlists = '%' + Description.get() + '%'
        dlists = '%' + Vin.get() + '%'
        c.execute("SELECT vRentalInfo.VIN, vRentalInfo.Vehicle, Avg(RATE.Daily) FROM RATE, vRentalInfo, VEHICLE WHERE (vRentalInfo.VIN = ? AND vRentalInfo.Vehicle = ?) AND RATE.Type = VEHICLE.Type AND RATE.Category = VEHICLE.Category AND VEHICLE.VehicleID = vRentalInfo.VIN;",(vlists,dlists,))
           
    print_records = ''
    labelList = [None] * 1000
    print_records = c.fetchall()
    for x,item in enumerate(print_records):
        labelList[x] = Label(root, text = item)
        labelList[x].grid(row = 4 + x, column = 0, columnspan = 2)
        
        
submit_button = Button(root, text = "Search",command = submit_lookup)
submit_button.grid(row = 3,column = 0,columnspan=2)
  
root.mainloop()  