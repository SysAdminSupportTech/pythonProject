#important note: time is generated in 3 format
#1 string using ctime() and asctime() 
#2 tuple using gmtime() and localtime()
#3 seconds using time() and calendar.timegm(localtime()/gmtime(since this produce a turple result))

from time import *
#this function discover the time epoc on your computer
def time1():
    print(time.gmtime(0))
#time1()

def time2():
    print(time())# this return the number of seconds after the epoc
#time2()

def time3():
    a = ctime() #display time in string
    print(a)
#time3()

def time4():
    a = time()
    b = ctime(a)
    print(b)

    time_tuple = (2019, 2, 26, 7, 6, 55, 1, 57, 0)
    time_obj = struct_time(time_tuple)
    print(time_obj)
#time4()

def time5():
    print(gmtime(1.99))
#time5()

def localtime1():
    current_local = localtime()
    print(current_local.tm_gmtoff)
#localtime1()

#converting time in using the calendar module
import calendar
def timesec():
    a = time()
    t = ctime()
    d = calendar.timegm(localtime())
    return d
#print(timesec())

#converting time.struct to string
def asctimef():
    a = asctime()
    b = asctime(localtime())
    print(b)
    print(a)
#asctimef()

def strftimef():
    a = strftime('%Y-%m-%d', localtime())
    print(a)
strftimef()