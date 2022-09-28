from tkinter import *

import mysql.connector

connection = mysql.connector.connect(host='localhost',port='3306',database='rentals',user='root',password='Superglide2')
c = connection.cursor(prepared=True)


root = Tk()
root.title("Customer Lookup")
root.geometry("400x600")
name = Entry(root, width = 30)
name.grid(row = 1, column = 1, padx=20)
id = Entry(root, width = 30)
id.grid(row = 2, column = 1, padx=20)
name_label = Label(root,text = "CustomerName")
name_label.grid(row = 1,column = 0)
id_label = Label(root,text = "CustomerID")
id_label.grid(row = 2,column = 0)

def submit_lookup():
    if (name.get() == ""):
        vlists = '%' + id.get() + '%'

        c.execute("SELECT vRentalInfo.CustomerName, vRentalInfo.CustomerID, vRentalInfo.RentalBalance FROM vRentalInfo WHERE vRentalInfo.CustomerID LIKE ? ORDER BY vRentalInfo.RentalBalance;",(vlists,))
      
    elif (id.get() == ""):
        dlists = '%' + name.get() + '%'

        c.execute("SELECT vRentalInfo.CustomerName, vRentalInfo.CustomerID, vRentalInfo.RentalBalance FROM vRentalInfo WHERE  vRentalInfo.CustomerName LIKE ? ORDER BY vRentalInfo.RentalBalance;",(dlists,))
    elif (name.get() == "" and id.get() == ""):

        c.execute("SELECT vRentalInfo.CustomerName, vRentalInfo.CustomerID, vRentalInfo.RentalBalance FROM vRentalInfo ORDER BY vRentalInfo.RentalBalance")
    else:
        vlists = '%' + name.get() + '%'
        dlists = '%' + id.get() + '%'
        c.execute("SELECT vRentalInfo.CustomerName, vRentalInfo.CustomerID, vRentalInfo.RentalBalance FROM vRentalInfo WHERE vRentalInfo.CustomerID LIKE ? AND vRentalInfo.CustomerName LIKE ? ORDER BY vRentalInfo.RentalBalance;",(dlists,vlists,))
           
    print_records = ''
    labelList = [None] * 1000
    print_records = c.fetchall()
    for x,item in enumerate(print_records):
        labelList[x] = Label(root, text = item)
        labelList[x].grid(row = 4 + x, column = 0, columnspan = 2)
        
        
submit_button = Button(root, text = "Search",command = submit_lookup)
submit_button.grid(row = 3,column = 0,columnspan=2)



root.mainloop()  

