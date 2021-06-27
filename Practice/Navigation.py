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
chdirs = os.listdir() #list directory in a readable format and assigning numbers to them
print("")
print("Current dir is {}".format(os.getcwd())) #Showing user the current directory he is working on
for dir in chdirs:
    print(chdirs.index(dir), "{}".format(dir))

print("")
userSelectFileFolder = int(input("SELECT A NUMBER TO A FILE OR FOLDER: "))
userOption  = chdirs[userSelectFileFolder]
if userSelectFileFolder:
    print("")
    print("You have Selected {}".format(userOption))
    print("")
    print("SELECT NUMBER BELOW TO PERFORM AN ACTION ON FILE OR DIRECTOR")
    btnActions = ["Size","FileType","Delete","Rename","New"]
    for btn in btnActions:
        print(btnActions.index(btn),"{}".format(btn))

    print("")
    #Creating a switch statement to handle actions
    userSelectActionBtn = int(input(""))
    if userSelectActionBtn == 0:
        fileSize = os.path.getsize(userOption)
        actualSize = fileSize / 1024
        print("FileSize: {}".format(actualSize))
    elif userSelectActionBtn == 1:
        fileType = os.path.splitext(userOption)
        fileTypeShow = fileType[1]
        print("FileType: {}".format(fileTypeShow))

    elif userSelectActionBtn == 2:
        os.remove(userOption)
        print("File: {} has been Deleted Successfully".format(userOption))
    elif userSelectActionBtn == 3:
        cwd = os.getcwd()
        filepath = cwd + "\\" + userOption
        renamedFile = os.rename(filepath, "NewFile.mp4")
        print("File: {} has been renamed to {}".format(userOption, renamedFile))
    elif userSelectActionBtn == 4:
        print("New has been selected")
    else:
        print("Non of The Action Button has been Selected. Please try again later.")

else:
    print('You Decide not to select anything. Get out of here and let us go')
