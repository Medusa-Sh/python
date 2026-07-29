#import necessary items
from tkinter import*
from tkinter import messagebox

#set up tkinter window
root=Tk()
root.geometry("200x200")

#Function for displaying warning message
#This will be called once the button is clicked
#message box.showwarning("Window name","Text to be displayed")
def msg():
    messagebox.showwarning("Alert","STOP! Virus found")

#Adding button widget to window
button=Button(root, text="scan virus", command=msg)
button.place(x=70,y=80)

#Entering main event roop
root.mainloop()