from tkinter import *
from datetime import date

# Create Window
root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')

# Add Label
lbl = Label(root, text="Hey There!", fg="white", bg="#072F5F", height=1, width=100)
lbl.pack()

# Add Label for name input
name_lbl = Label(root, text="Enter your name ", bg="#3895D3", width=400)
name_lbl.pack()

# Entry widget
name_entry = Entry(root, width=30)
name_entry.pack(pady=10)

# Text Widget to display message
text_box = Text(root, height=5, width=45)
text_box.pack(pady=10)

# Function to display greeting
def display():
    name = name_entry.get()
    if name.strip():  # Check if name is not empty
        text_box.delete('1.0', END)  # Clear previous text
        greet = f"Hello {name}\n"
        message = f"Welcome to the Application!\nToday's date is: {date.today()}"
        text_box.insert(END, greet + message)
    else:
        text_box.delete('1.0', END)
        text_box.insert(END, "Please enter your full name.")

# Button
btn = Button(root, text="Begin", command=display, bg="#1261A0", fg='white')
btn.pack()

# Start the GUI loop
root.mainloop()
