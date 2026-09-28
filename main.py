# Import necessary libraries
from tkinter import *
# Create window
window = Tk()
window.title("Event Handler")
window.geometry("100x100")
# Event handler for button click
def handle_click(event):
    print("\nThe button was clicked!")
    print("Hello")

button = Button(text="Click me!")
button.pack()

# Bind click event to handle_click()
button.bind("<Button-1>", handle_click)
window.mainloop()
