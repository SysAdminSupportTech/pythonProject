from tkinter import *
window = Tk()
window.title("TKinter Button Action")
#defining tk_btn action
def tk_btn():
    Selected = "YOu have submitted and action"
    print(Selected)

#Creating the button action
button = Button(text="submit", fg="white", bg="black", command=tk_btn).pack()
label = Label()
label.pack()

window.mainloop()