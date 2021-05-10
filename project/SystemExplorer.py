#Declaring System Explorer function
import os
def mainApp():
    #Setting user root to home directory
    homedir = os.path.expanduser("~")
    print("This is the user Current directory {}".format(homedir))
mainApp()