# Import necessary libraries
from tkinter import *

# Create Window
root = Tk()
root.title('Age app')
root.geometry('400x300')

# Add widgets
# Add Label 
lbl = Label(text="Enter your information", fg="white", bg="#072F5F", height=1, width=300)

# Add Label for getting name as input from user
# Use Entry Widget to create a text box for user to enter details
name_lbl = Label(text="Full Name", bg="#3895D3")
name_entry = Entry()
age_lbl = Label(text="Age", bg="#3895D3")
age_entry = Entry()
month_lbl = Label(text="month", bg="#3895D3")
month_entry = Entry()
date_lbl = Label(text="date", bg="#3895D3")
date_entry = Entry()
# Function to display a Message
def display():
	# Read input given by user
	name = name_entry.get()
	date=date_entry.get()
	age=age_entry.get()
	month=month_entry.get()
	global message
	message = "Welcome to the Application! \nYour are:""+name+age+date+month"

	text_box.insert(END, message)

# Add a Text Widget to display information/messages
text_box = Text(height=3)


name_lbl.pack()
date_lbl.pack()
month_lbl.pack()
age_lbl.pack()
root.mainloop()