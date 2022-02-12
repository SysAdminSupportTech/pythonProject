#! /usr/bin/env python3

#Disk value convertion
#Note: When converting from bytes upward, we divide the numbert of byte(1024) by 1024^2(mb)
#1023^3(Convert to GB) etc.
#When converting from GB <- B, we multiply the value by 1024
#General Fomular for converting from Bytes to GB = B/1024^2
#https://www.to-convert.com/en/computer/convert-byte-to-mb.php
import psutil as psu
def comp_monitor():
    """This programs monitor some specific computer hardware resources."""
    print("DISK STATISTICS")
    diskusage = psu.disk_usage("/")
    disk_size, space_used, space_remaining, percentage = diskusage
    GB = 1024 ** 3
    disksize = disk_size / GB
    usedspace = space_used / GB
    spaceremain = space_remaining / GB
    print("Total Disk Size: = ", round(disksize, 2))
    print("Used Disk Space =", round(usedspace, 2))
    print("Free Space =", round(spaceremain, 2))
    print("Disk Percentage(%) =", percentage)
    

print(comp_monitor())