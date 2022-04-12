from cgitb import text
from textwrap import fill
import tkinter as tk
from tracemalloc import start
pcanvas = tk.Tk()
pcanvas.geometry("300x300")
c=tk.Canvas(pcanvas, bg="blue", height=250, width=250)
cord = 10, 50, 240, 210 
arc = c.create_arc(cord, start=0, extent=270, fill="red")

traingle = c.create_rectangle(200,100,5,5)
c.pack()
pcanvas.mainloop()