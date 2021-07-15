import time #import the time module
def seperator():
    print("")
    print(80*"-")
    print("")

print("This is my computer Epoc System time: ", time.gmtime(0))#knowing my system epoc time
seperator() #function
print("My System current time:", time.time())
seperator() #function
print("Representing time in string format")
gettime = time.time()
print("Your Time in string Format is: {}".format(time.ctime(gettime)))
seperator() #function
print("Working With Local Time ")
print("This is my local time", time.localtime(gettime))
seperator() #function
print(time.asctime())
seperator() #function
print("output time in format you want")
timeformat= time.time()
print(time.strftime("%Y/%m/%d", time.localtime()))



