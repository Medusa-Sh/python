#import neccesary libraries 
from tkinter import *

#setting up the main window
root=Tk()
root.geometry('400x300')
root.title("MAIN")

#Function to open the new(toplevel) window
def top_town():
    top=Toplevel()
    top.geometry("180x180")
    top.title("toplevel")


    #Adding a label to the new window
    l2=Label(top,text="This is toplevel window")
    l2.pack()

    top.mainloop()


l=Label(root,text="This is root window")
btn=Button(root,text="open toplevel window",command=top_town)

l.pack()
btn.pack()
root.mainloop()