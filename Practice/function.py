#Writting my first function
def printHello(fname, lname):
    print("Welcome Mr." + fname + lname)
#printHello("Albert ","Eromosele")

#Working with numbers of unknown arguments
def printMessage(*kid):
    print("The youngest child is " + kid[3])

#printMessage("Albert","Eromosele","Job","Loyalty", "Barrah")

#Using Default Parameter Values
def default_param(country = "Nigeria"):
    print("Im from {} country".format(country))
#default_param("Canada")

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
#tri_recursion(6)

def homedir():
  from os.path import expanduser
  home = expanduser("~")
  return home
#homedir()

def homedir2():
  import os
  home = os.path.expanduser("~user")
  return home
#homedir2

#**********************************************************************
import os
#print(os.name)
#print(os.environ)
print(os.environ["HOMEPAT"])
print("This is the function of os.getenv" + os.getenv("HOMEPATH"))



