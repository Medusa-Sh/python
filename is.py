from tkinter import *
from tkinter import Toplevel
import datetime

main=Tk()
toplevel= Toplevel()
main.title("Main window")
main.geometry("400x400")
toplevel.title("Toplevel window")
toplevel.geometry("200x200")
def code():
    now = datetime.datetime.now()
    label=Label(text=f"Current date and time: {now}")
    label.pack()
    label1=Label(text="You need to read 15 pages of the book")
    label1.pack()

def open_toplevel():
    toplevel.deiconify()
    label2=Label(toplevel,text=f"It will take {100//15} days to finish the book.")
    label2.pack()

btn=Button(main,text="Click to see the current time and today's objectives"
           ,command=code,bg="blue",fg="black")
btn.pack()
toplevel.withdraw()
btn1=Button(main,text="Click to see how many days " \
"it will take to finish the book",command=open_toplevel,bg="green",fg="white")
btn1.pack()
main.mainloop()
