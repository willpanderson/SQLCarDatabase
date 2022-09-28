from tkinter import *

import mysql.connector

connection = mysql.connector.connect(host='localhost',port='3306',database='rentals',user='root',password='Superglide2')
c = connection.cursor(prepared=True)
root = Tk()
root.title("Add New Customer")
root.geometry("400x400")
f_name = Entry(root, width = 30)
f_name.grid(row = 0, column = 1, padx=20)
phone = Entry(root, width = 30)
phone.grid(row = 1, column = 1)

fname_label = Label(root,text = "Customer Name")
fname_label.grid(row = 0,column = 0)
phone_label = Label(root,text = "Customer Phone #")
phone_label.grid(row = 1,column = 0)


def submit():
    c.execute("INSERT INTO customer(Name, Phone) VALUES(?,?)",(f_name.get(),phone.get(),))
    c.execute("Select customer.CustID from customer where customer.Name = ?",(f_name.get(),))
    ID = c.fetchall()
    test = ("Hi " + str(f_name.get()) + ", your Customer ID is:" + str(ID))
    response_label = Label(root,text = test)
    response_label.grid(row = 3,column = 1)
    f_name.delete(0,END)
    phone.delete(0,END)
   

submit_button = Button(root, text = "Add New Customer",command = submit)
submit_button.grid(row = 2,column = 0,columnspan=2)

root.mainloop() 
