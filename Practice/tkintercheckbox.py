from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('200x80')

def isChecked():
    if cb.get() == 1:
        btn['state'] = NORMAL
    else:
        btn['state'] = DISABLED
cb = IntVar()

Checkbutton(ws, text="accept T&C", variable=cb, onvalue=1, offvalue=0, command=isChecked).pack()
btn = Button(ws, text='Sleeping!', state=DISABLED, padx=20, pady=5)
btn.pack()

ws.mainloop()

"""
window = Tk()
window.geometry("240x240")

def isChecked():
    if var.get() == 1:
        btn['state'] = NORMAL
        btn.configure(text="Alive")
    else:
        btn['state'] = DISABLED

var = IntVar()
cbox = Checkbutton(text="Enable",variable=var, onvalue=1, offvalue=0, command=isChecked).pack()
btn = Button(text="Submit", state=DISABLED, command='').pack()

window.mainloop()
"""