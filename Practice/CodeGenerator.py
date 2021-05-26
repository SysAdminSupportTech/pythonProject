import os
hiddenMessage = "Your encryption password is: DONE05324"
usernameMessage = input("Enter Your Username to verift who you are: ")
print("Welcome Mr : {}".format(usernameMessage))

#Add User Name to a file
username = open("username.txt","a") #Write code to a text editor
username.write("\n{}".format(usernameMessage))

userinput1 = input("why are you here: ")
if userinput1 == 'code':
    print("Mr {}, it shows you are here to get your secrete pass".format(usernameMessage))
    userinput2 = input("Enter The Last 4 digit to claim your code:")
    usrvalue = "DONE0" + userinput2 
    print(usrvalue)
    if  usrvalue == "DONE05324" :
       print(hiddenMessage)
    else:
        print("Sorry you Enter a wrong value.... Goodbye")
else:
    print("Thank you for stopping by Mr: {}".format(usernameMessage))