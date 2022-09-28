from tkinter import *

import mysql.connector

connection = mysql.connector.connect(host='localhost',port='3306',database='rentals',user='root',password='Superglide2')
c = connection.cursor(prepared=True)


root = Tk()
root.title("Make Payment")
root.geometry("400x600")
name = Entry(root, width = 30)
name.grid(row = 1, column = 1, padx=20)
vin = Entry(root, width = 30)
vin.grid(row = 2, column = 1)
return_date = Entry(root, width = 30)
return_date.grid(row = 3, column = 1)
payment = Entry(root, width = 30)
payment.grid(row = 4, column = 1)

name_label = Label(root,text = "Customer Name")
name_label.grid(row = 1,column = 0)
vin_label = Label(root,text = "VIN")
vin_label.grid(row = 2,column = 0)
return_label = Label(root,text = "Return Date")
return_label.grid(row = 3,column = 0)
payment_label = Label(root,text = "Payment Amount")
payment_label.grid(row = 4,column = 0)
       
def submit_payment():
    Payment = payment.get()
    int(Payment)
    c.execute("Update rental,customer set rental.TotalAmount = (rental.TotalAmount - ? ) where customer.CustID = rental.CustID and rental.VehicleID = ? and customer.Name = ? and rental.ReturnDate = ?",(Payment,vin.get(),name.get(),return_date.get(),))
    c.execute("Select rental.TotalAmount from rental where rental.VehicleID = ? and rental.ReturnDate = ? ",(vin.get(),return_date.get(),))
    amount = c.fetchall()
    response = Label(root,text = ("Your balance is " + str(amount)))
    response.grid(row=6,column=0)
submit_button = Button(root, text = "Search",command = submit_payment)
submit_button.grid(row = 5,column = 0,columnspan=2)

root.mainloop()  