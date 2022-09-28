from tkinter import *

import mysql.connector
import os 

connection = mysql.connector.connect(host='localhost',port='3306',database='rentals',user='root',password='Superglide2')
c = connection.cursor(prepared=True)
root = Tk()
root.title("Add New Rental")
root.geometry("500x700")

hint = Label(root, text = "Type:(0:Basic,1:Luxury) Category(1:Compact,2:Medium,3:Large,4:SUV,5:Truck,6:Van)")
hint.grid(row = 0, column = 0, columnspan = 2)

custid = Entry(root, width = 30)
custid.grid(row = 1, column = 1, padx=20)
vin = Entry(root, width = 30)
vin.grid(row = 2, column = 1)
start = Entry(root, width = 30)
start.grid(row = 3, column = 1)
order = Entry(root, width = 30)
order.grid(row = 4, column = 1)
type = Entry(root, width = 30)
type.grid(row = 5, column = 1)
qty = Entry(root, width = 30)
qty.grid(row = 6, column = 1)
returnday = Entry(root, width = 30)
returnday.grid(row = 7, column = 1)
paymentdate = Entry(root, width = 30)
paymentdate.grid(row = 8, column = 1)
total = Entry(root, width = 30)
total.grid(row = 9, column = 1)

id_label = Label(root,text = "Customer ID")
id_label.grid(row = 1,column = 0)
vin_label = Label(root,text = "VIN")
vin_label.grid(row = 2,column = 0)
start_label = Label(root,text = "Start Date (YYYY-MM-DD)")
start_label.grid(row = 3,column = 0)
order_label = Label(root,text = "Order Date (YYYY-MM-DD)")
order_label.grid(row = 4,column = 0)
type_label = Label(root,text = "Rental Type (1:Daily,7:Weekly)")
type_label.grid(row = 5,column = 0)
qty_label = Label(root,text = "Quantity")
qty_label.grid(row = 6,column = 0)
return_label = Label(root,text = "Return Date (YYYY-MM-DD)")
return_label.grid(row = 7,column = 0)
paymentd_label = Label(root,text = "Payment Date (YYYY-MM-DD)")
paymentd_label.grid(row = 8,column = 0)
paymentd_label = Label(root,text = "Total Amount")
paymentd_label.grid(row = 9,column = 0)
def submit():
    if(paymentdate.get() == order.get()):
        os.system('subcode4b.pyw')
    c.execute("INSERT INTO rental(CustID, VehicleID, StartDate, OrderDate, RentalType, Qty, ReturnDate,TotalAmount, PaymentDate)VALUES (?,?,?,?,?,?,?,?,?);",(custid.get(),vin.get(),start.get(),order.get(),type.get(),qty.get(),returnday.get(),total.get(),paymentdate.get(),))
    response_label = Label(root,text = "The reservation has been entered into the system.")
    response_label.grid(row = 11,column = 1)
submit_button = Button(root, text = "Add New Rental",command = submit)
submit_button.grid(row = 10,column = 0,columnspan=2)

root.mainloop() 


