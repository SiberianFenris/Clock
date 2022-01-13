from tkinter import *
from tkinter.ttk import *
from time import strftime


root = Tk()
root.title("Clock")
root.geometry("800x600")
root.config(background = "black")

def time():
    str = strftime('%H:%M:%S %p')
    label.config(text=str)
    label.after(1000, time)


label = Label(root, font=("ds-digital", 100), background="black", foreground="cyan", text = "Middle")
label.pack(anchor = 'center', pady=200)


time()

mainloop()