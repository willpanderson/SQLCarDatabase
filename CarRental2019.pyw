import os


from tkinter import *

root = Tk()
root.title("CarRental2019")
root.geometry("300x300")

def add_customer():
	os.system('subcode1.pyw')
def add_vehicle():
	os.system('subcode2.pyw')
def see_rental():
	os.system('subcode3a.pyw')	
def add_rental():
	os.system('subcode3b.pyw')	
def return_rental():
	os.system('subcode4a.pyw')
def make_payment():
	os.system('subcode4b.pyw')
def view_customer():
	os.system('subcode5.pyw')
def view_vehicles():
	os.system('subcode5b.pyw')

customer_button = Button(root, text = "Add Customer",command = add_customer)
customer_button.grid(row = 1,column = 1,columnspan=2)

vehicle_button = Button(root, text = "Add Vehicle",command = add_vehicle)
vehicle_button.grid(row = 2,column = 1,columnspan=2)

see_button = Button(root, text = "See Avalible Rentals",command = see_rental)
see_button.grid(row = 3,column = 1,columnspan=2)

rental_button = Button(root, text = "Add Rental",command = add_rental)
rental_button.grid(row = 4,column = 1,columnspan=2)

returnrental_button = Button(root, text = "Return Rental",command = return_rental)
returnrental_button.grid(row = 5,column = 1,columnspan=2)

payment_button = Button(root, text = "Make Payment",command = make_payment)
payment_button.grid(row = 6,column = 1,columnspan=2)

vcustomer_button = Button(root, text = "Customer Lookup",command = view_customer)
vcustomer_button.grid(row = 7,column = 1,columnspan=2)

vvehicle_button = Button(root, text = "Vehicle Lookup",command = view_vehicles)
vvehicle_button.grid(row = 8,column = 1,columnspan=2)


root.mainloop()  