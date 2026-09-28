from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("500x500")
def msg():

    messagebox.showwarning("alert!","Stop! Virus Found.")
def msg1():

    messagebox.showerror("Error","Error Found Please check code.")  
def msg2():

    messagebox.showinfo("Info ","Display Information.")  
def msg3():

    messagebox.askquestion("Ask  ","Are you ready for dare ?")  
def msg4():

    messagebox.askokcancel("Ask  ","select your option  ?")    

button = Button(root, text="Scan for virus", command=msg)
button.place(x=40, y=50)
button = Button(root, text="Error Message ", command=msg1)
button.place(x=40, y=100)
button = Button(root, text="Show Info", command=msg2)
button.place(x=40, y=150)
button = Button(root, text="Ask Question", command=msg3)
button.place(x=40, y=200)
button = Button(root, text="Ask Ok Cancel", command=msg4)
button.place(x=40, y=250)
root.mainloop()