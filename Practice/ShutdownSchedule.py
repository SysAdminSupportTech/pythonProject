from tkinter import *
import os
import time

window = Tk() #initializing the window class
window.title("Shutdown Scheduler")
window.geometry("350x230")
label_top = Label(bg="white",fg="white", width= 100, height=15).pack()
#time Text entry value
time_label = Label(text="Enter Time in Hours")
time_label.place(x=100, y=5)
time_entry = Entry(window)
#Getting the value of morning
def schedule():
    """
        Use powershell to schedule the shutdown
    """
    selected = time_entry.get()
    time_call = 60*60*int(selected)
    timer= str(time_call)
    os.system('shutdown /s /t ' + timer)

def btn_cancel():
    pass

time_entry.place(x=50, y=30, width= 250, height=25)
#Creating Check button strict and Mild
var = IntVar()
strict = Radiobutton(window, text="STRICT", variable=var, value=1)
strict.place(x=100, y=80)
mild = Radiobutton(window, text="MILD", variable=var, value=2)
mild.place(x=180, y=80)

#Creating the schedule button
button_submit = Button(text="Schedule", background="green", fg="white",font=12, command=schedule).place(x=12, y=150)
button_reschedule = Button(text="Reschedule", background="grey", fg="white", font=12).place(x=120, y=150)
button_cancel = Button(text="Cancel", bg="red",fg="black", font=12).place(x=250, y=150)


label = Label(window)
label.pack()
window.resizable(False,False)


window.mainloop()