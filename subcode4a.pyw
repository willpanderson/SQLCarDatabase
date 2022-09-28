from tkinter import *

import mysql.connector


connection = mysql.connector.connect(host='localhost',port='3306',database='rentals',user='root',password='Superglide2')
c = connection.cursor(prepared=True)


root = Tk()
root.title("Return Rental")
root.geometry("400x600")
name = Entry(root, width = 30)
name.grid(row = 1, column = 1, padx=20)
vin = Entry(root, width = 30)
vin.grid(row = 2, column = 1)
return_date = Entry(root, width = 30)
return_date.grid(row = 3, column = 1)
name_label = Label(root,text = "Customer Name")
name_label.grid(row = 1,column = 0)
vin_label = Label(root,text = "VIN")
vin_label.grid(row = 2,column = 0)
return_label = Label(root,text = "Return Date")
return_label.grid(row = 3,column = 0)

       
def submit():
   c.execute("SELECT Customer.CustID, Customer.Name, rental.VehicleID, rental.TotalAmount, rental.ReturnDate FROM RENTAL, Customer, Vehicle WHERE Customer.Name = ? AND rental.vehicleID = ? AND rental.ReturnDate = ?;",(name.get(),vin.get(),return_date.get(),))
   c.execute("UPDATE rental SET returned = 1 where Customer.Name = ? AND rental.vehicleID = ? AND rental.ReturnDate = ?",(name.get(),vin.get(),return_date.get(),))
   response = Label(root,text = "Your rental is now closed. Thank you for choosing CarRental2019")
   response.grid(row=5,column=0)
submit_button = Button(root, text = "Return Rental",command = submit)
submit_button.grid(row = 4,column = 0,columnspan=2)

root.mainloop()  
