from cgitb import text
import tkinter as tk
gpos = tk.Tk()
gpos.geometry("250x250")
checkVar1 = tk.IntVar()
checkVar2 = tk.IntVar()

tk.Checkbutton(gpos, text="Machine Learning", variable=checkVar1, onvalue= 1, offvalue=0).grid(row=0)
tk.Checkbutton(gpos, text="Deep Learning", variable=checkVar2, onvalue=0, offvalue=1).grid(row=1,column=1)

gpos.mainloop()