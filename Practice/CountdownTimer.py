#Welcome to our countdown timer
#What im expected to learn from this practice
#1. How to use the time module
#2. How to use While loop
#3. How to use the divMode() function
#4. HOw to use End =\r
#5. How to use the time.sleep() function

import time
def countdown(t):
    while t:
        min, sec = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(min, sec)
        print(timer, end="\r")
        time.sleep(1)
        t-=1
    print("fire in the hole")
t = input("Input time in seconds: ")

print(countdown(int(t)))