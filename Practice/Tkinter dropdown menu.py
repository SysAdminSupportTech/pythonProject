#Tkinter dropdown menu
import tkinter as tk
from typing import Text
window = tk.Tk() #initiat the class

window.geometry("200x200") #Setting the size of the window
window.title("DropDown") #window title

def show():
    label.config(text = clicked.get())

options = [
    "Monday",
    "Tuesday",
    "wednessday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

#data type of Menu text
clicked = tk.StringVar()

#Initiat the first selected option
clicked.set("Monday")

drop = tk.OptionMenu(window, clicked, *options)
drop.pack()

#Creating a button for the program.
button = tk.Button(window, text="Scheduled", command=show).pack()
#Create Label
label = tk.Label(window, text=" ")
label.pack()

window.mainloop()