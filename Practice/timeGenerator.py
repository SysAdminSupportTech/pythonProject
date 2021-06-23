#Write some code that can take two dates as input, and calculate the amount of time between them. This will be a great way to familiarize yourself with Python's datetime module.
import time
import datetime
def wtime():
    a=time.time()
    print(a)
    b=time.ctime(a)
    print(b)
    print("\n\n")
    c=time.localtime()
    print('Local time format with 9 classes')
    d=time.asctime(c)
    print(d)
    print("\n\n")
    e=time.strftime("%d/%m/%Y")
    print(e)
    help(time.strftime)
#wtime()

def wdatetime():
    print("\n\n")
    print("working with Datetime.today")
    f=datetime.datetime.today()
    print(f)
    print("\n\n")
    print("working with Datetime.now")
    g=datetime.datetime.now()
    print(g)
    print("\n\n")
    print("working with Datetime.date")
    h=datetime.date(2020,8,7)
    print(h)
    print("\n\n")
    print("working with Datetime time difference")
    b1 = datetime.timedelta(days=20)
    b2 = datetime.timedelta(days=31)
    b3 = b1-b2
    print(b3)
    print("\n\n")
    print("working with Datetime fuction")
wdatetime()



