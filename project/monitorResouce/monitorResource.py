#Get CPU Utilization
from cgitb import text
from re import X
from turtle import bgcolor, color
import psutil as psu
import time
import threading # this allows me to run while loops in parrallel
import tkinter as tk

def cpu_utilization():
    """
        This handles the cpu utilization on my computer
    """
    while True:
        cpu_util = psu.cpu_percent(interval=0.5)
        print("CPU Utilization: {} %".format(cpu_util), end="\r")


def RAM_utilization():
    """ 
        This function handles the RAM Utilization of the computer
    """
    while True:
        RAM_usage = psu.virtual_memory()
        print("RAM Utilization: {}".format(RAM_usage[2]), end="\r")
        

def disk_utilization():
    """
        This function print out the disk utilization of a computer
    """
    while True:
        disk_usage = psu.disk_usage('/')
        print("Disk Utilizatioin: {}".format(disk_usage[3]), end="\r")


#thread1 = threading.Thread(target=cpu_utilization)
#thread1.start()

#Working With the TKinter GUI
RProgram = tk.Tk()
RProgram.geometry("300x300")
RProgram.title("Resource Monitor")
RProgram.resizable(False,False)
cbox = tk.Canvas(RProgram, bg="black", height=300, width=300) #Declaring the canvas
title_nav = tk.Frame(RProgram, bg="white", height=15).pack() #title frame
title_label = tk.Label(title_nav, text="Resource Window Monitor", background="black",foreground="white", width=300).pack()
CPU_Frame = tk.Frame(RProgram).pack() #CPU Frame
CPU_Label = tk.Label(CPU_Frame, text="CPU_UTILIZATION").place(x="6", y="43",height=40, width=120)

CPU_entry = tk.Entry(RProgram).place(x="130", y="43",height=40, width=164)

disk_Frame = tk.Frame(RProgram).pack()
disk_Label = tk.Label(disk_Frame, text="Disk_UTILIZATION").place(x="6", y="92",height=40, width=120)

RAM_Frame = tk.Frame(RProgram).pack()
RAM_Label = tk.Label(disk_Frame, text="RAM_UTILIZATION").place(x="6", y="145",height=40, width=120)

other_proc = tk.Frame(RProgram, background="black", bg="white").place(x=6, y=200, height=90, width=286)
high_proc_label =tk.Label(other_proc, text="High Processes").place(x=6, y=200, height=90, width=120)

pro_label = tk.Label(other_proc, text="Process Name").place(x=125, y=200, width=120)
pro_label2 = tk.Label(other_proc, text=" %").place(x=238, y=200, width=50)



cbox.pack() #Canvas frame closed
RProgram.mainloop() #Initialize program