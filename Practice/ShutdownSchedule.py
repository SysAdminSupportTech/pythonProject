from tkinter import *

window = Tk() #initializing the window class
window.title("Shutdown Scheduler")
window.geometry("350x230")
label_top = Label(bg="white",fg="white", width= 100, height=15).pack()
#Creating a dropdown list
schedule_time_morning = [
    "Morning",
    "00:00 AM",
    "01:00 AM",
    "01:30 AM",
    "02:00 AM",
    "02:30 AM",
    "03:00 AM",
    "03:30 AM",
    "04:00 AM",
    "05:00 AM",
    "05:30 AM",
    "06:00 AM",
    "06:30 AM",
    "07:00 AM",
    "07:30 AM",
    "08:00 AM",
    "08:30 AM",
    "09:00 AM",
    "09:30 AM",
    "10:00 AM",
    "10:30 AM",
    "11:00 AM",
    "11:30 AM",
]

schedule_time_afternoon = [
    "Afternoon",
    "12:00 PM",
    "12:30 PM",
    "01:00 PM",
    "01:30 PM",
    "02:00 PM",
    "02:30 PM",
    "03:00 PM",
    "03:30 PM",
    "04:00 PM",
    "04:30 PM",
    "05:00 PM",
    "05:30 PM",
    "06:00 PM",
    "06:30 PM",
    "07:00 PM",
    "07:30 PM",
    "08:00 PM",
    "08:30 PM",
    "09:00 PM",
    "10:30 PM",
    "11:00 PM",
    "11:30 PM",
    "12:00 PM",
    "12:30 PM"
]
#Getting the value of morning
def schedule_morning():
    pass

clicked_morning = StringVar()
clicked_morning.set(schedule_time_morning[0])
dropdown_morning = OptionMenu(window,clicked_morning, *schedule_time_morning)
dropdown_morning.place(x=50, y=10)

clicked_afternoon = IntVar()
clicked_afternoon.set(schedule_time_afternoon[0])
dropdown_afternoon = OptionMenu(window,clicked_afternoon, *schedule_time_afternoon)
dropdown_afternoon.place(x=200, y=10)

#Creating Command action
def action():
    selected = "you have done well" + str(var.get())
    label.config(text = selected)

#Creating Check button strict and Mild
var = IntVar()
strict = Radiobutton(window, text="STRICT", variable=var, value=1, command=action)
strict.place(x=100, y=80)
mild = Radiobutton(window, text="MILD", variable=var, value=2, command=action)
mild.place(x=180, y=80)

#Creating the schedule button
button_submit = Button(text="Schedule", background="green", fg="white",font=12, command=schedule_morning).place(x=12, y=150)
button_reschedule = Button(text="Reschedule", background="grey", fg="white", font=12).place(x=120, y=150)
button_cancel = Button(text="Cancel", bg="red",fg="black", font=12).place(x=250, y=150)


label = Label(window)
label.pack()
window.resizable(False,False)


window.mainloop()