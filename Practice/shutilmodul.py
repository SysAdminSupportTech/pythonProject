from turtle import clear
import psutil as psu
import socket
print("DISK INFORMATION:")
diskusage = psu.disk_usage("/")

disk_size, space_used, space_remaining, percentage = diskusage
print("Total Disk Size: = ", disk_size)
print("Used Disk Space =", space_used)
print("Free Space =", space_remaining)
print("Disk Percentage(%) =", percentage)


