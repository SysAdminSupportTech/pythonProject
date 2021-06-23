import datetime
import time
def CalDateDiff():
    print("Welcome our program that calculate date differences")
    fdate = float(input("Enter the first date(YYYY,m,day): "))
    sdate = float(input("Enter the second date(YYYY,m,day): "))
    convertuserinput1 = datetime.date(float(fdate))
    convertuserinput2 =datetime.date(sdate)
    result = convertuserinput1 - convertuserinput2
    print(result)
CalDateDiff()
