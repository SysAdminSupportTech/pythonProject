import tkinter as tk
window = tk.Tk()
"""
window.geometry("350x500")

test = tk.Label(window, text='red', bg="red", fg='white')
test.pack(side=tk.BOTTOM)

test2 = tk.Label(window, text="green", bg="white", fg='black')
test2.pack(side=tk.BOTTOM )

test3 = tk.Label(window, text="red", bg="red", fg="white")
test3.pack(padx=10, pady=100, side=tk.RIGHT)
window.mainloop()"""

window.geometry("250x250+250+250")
tk.Label(window, text="Position 1: x=0, y=0", bg="black", fg="white").place(x=5, y=0)
tk.Label(window, text="Position 2: x=50, y=40", bg="Purple", fg="white").place(x=200, y=0)

window.mainloop()