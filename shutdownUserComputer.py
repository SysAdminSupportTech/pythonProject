#This program is design to shut down you computer

#Os module required for this to work
import os 

#user Message
usrinput = input("Do you want to shutdown your computer (n/y): ")
if usrinput == 'y':
    confirmation = input("Type 'yes' complete in lower case to confirm you want to shutdown:  ")
    if confirmation == 'yes':
        os.system('shutdown /s /t 1')
    else:
        print('you are a wise man/woman')
else:
    print("You computer will not shutdown... Program exit 0x0")
    exit()

