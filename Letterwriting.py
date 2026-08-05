from tkinter import*
from tkinter.filedialog import askopenfilename,asksaveasfilename
root=Tk()
root.title("Letter writing application")
root.geometry('400x400')

def open_file():
    askopenfilename(title="select a file",filetypes=[("Text files","*.txt")])
    
def save_file():
    asksaveasfilename(title="Save as...",filetypes=[("Text files","*.txt")])
    
btn=Button(root,text="open file",command=open_file)
btn.pack()
btn2=Button(root,text="save file",command=save_file)
btn2.pack()
root.mainloop()