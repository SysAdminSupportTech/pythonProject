import os
from posixpath import join
message = "\nWelcome to our computer navigation system. This program allow you to navigate to different directory on the computer\n"
print(message)
#1. Get Current User Directory
home = os.getcwd()
print("Your Current Work space is {}".format(home))
#2. Ask user if he want to change his current dir
userChangeDirMessage = input("Do you want to Work with the Current Work space (Y\'N) : ")
if userChangeDirMessage.upper() == 'Y':
    #showing the content of user Current Working Dir
    userWorkSpace = os.listdir(home)
    print(userWorkSpace)
else:
    #Change user path to home Directory
    homedir = os.path.expanduser("~")
    os.chdir(homedir) #Set Current Home dir
    Cdir = os.getcwd() #Get Current Home Dir
    print("Your Current directory is {}\n".format(Cdir))
    dirs = os.listdir(homedir) #Nesting all folder directories inside the dirs variable
    for dir in dirs: # Looping through my directory to set corresponding numbers to name of directories
        print(dirs.index(dir),"{}".format(dir))
    
#Ask Users to Select a number based on the value above
print('\n') #escape Character
userChoice = int(input("SELECT A NUMBER FROM THE LIST ABOVE TO OPEN FOLDER/FILE: "))
userPickedVal = dirs[userChoice]
#Select Directory based on Value selected
SetUserDirofChoice = homedir + "\\" + userPickedVal #Append user directory choice to home dir
os.chdir(SetUserDirofChoice) #Set path to user directory choice
print(os.listdir())
