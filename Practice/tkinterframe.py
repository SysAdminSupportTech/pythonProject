from cgitb import text
import tkinter as tk
pframe = tk.Tk()
pframe.title("Working with my Frame")
pframe.geometry("250x250")
tp_fr=tk.Frame(pframe).pack()
bt_fr=tk.Frame(pframe).pack(side= "bottom")

btnl=tk.Button(tp_fr, text="Button1", bg="Green").pack()
btn2=tk.Button(bt_fr, text="Button2", bg="Black").pack()
btn3=tk.Button(bt_fr, text="Button3", bg="Orange").pack(side= "left")
btn4=tk.Button(bt_fr, text="Button4", bg="Pink").pack(side="left")
pframe.mainloop()