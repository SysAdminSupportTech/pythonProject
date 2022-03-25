#Get CPU Utilization
import psutil as psu
import time
import threading # this allows me to run while loops in parrallel

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
