#! /usr/bin/env python3

#Disk value convertion
#Note: When converting from bytes upward, we divide the numbert of byte(1024) by 1024^2(mb)
#1023^3(Convert to GB) etc.
#When converting from GB <- B, we multiply the value by 1024
#General Fomular for converting from Bytes to GB = B/1024^2
#https://www.to-convert.com/en/computer/convert-byte-to-mb.php
from dataclasses import dataclass
import psutil as psu
import os
import datetime
def disk_info():
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
    

def netConn():
    netConn = psu.net_connections()
    for conn in netConn:
        print(conn)


def nic_interface():
    print("Example 3: Print the NIC Information")
    nic_conn = psu.net_if_addrs()
    print(nic_conn)

def boot_time():
    print("Example 4: Print the Computer boot time")
    boot_time = psu.boot_time()
    #converting the boot time in seconds
    convert_boottime = datetime.datetime.fromtimestamp(boot_time).strftime("%Y-%m-%d %H:%M:%S")
    print(convert_boottime)


def get_users():
    print("Example 5: Get Users Details")
    users = psu.users()
    for detail in users:
        print(detail)
    #users_logon = datetime.datetime.fromtimestamp(logon_time).strftime("%Y-%m-%d %H:%M:%S")

def get_pid():
    print("Example 5: Get PIDs")
    for i in psu.process_iter(['pid', 'name', 'username']):
        print(i)
get_pid()