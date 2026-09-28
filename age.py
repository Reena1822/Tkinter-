from tkinter import *
import datetime

root = Tk()
root.title("Age Calculator App")
root.geometry("400x350")

Label(root, text="Enter birth year:", fg="white", bg="#072f5f", height=1, width=100).pack()
year_entry = Entry(root, width=30)
year_entry.pack(pady=10)

Label(root, text="Enter birth month (1-12):", bg="#3895d3", width=400).pack(pady=10)
month_entry = Entry(root, width=30)
month_entry.pack(pady=10)

Label(root, text="Enter birth day (1-31):", fg="white", bg="#072f5f", height=1, width=100).pack()
day_entry = Entry(root, width=30)
day_entry.pack(pady=10)

text_box = Text(root, height=2, width=45)
text_box.pack(pady=10)

def display():
    text_box.delete("1.0", END)
    try:
        y = int(year_entry.get().strip())
        m = int(month_entry.get().strip())
        d = int(day_entry.get().strip())
        birth_date = datetime.date(y, m, d)  # will raise ValueError if invalid
        today = datetime.date.today()

        age = today.year - birth_date.year
        # subtract 1 if birthday this year hasn't occurred yet
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        if age < 0:
            text_box.insert(END, "Birth date is in the future.")
        else:
            text_box.insert(END, f"Your age is: {age}")
    except ValueError:
        text_box.insert(END, "Please enter a valid date (YYYY, MM, DD).")

Button(root, text="Calculate Age", command=display, bg="#1261a0", fg="white").pack(pady=5)

root.mainloop()
