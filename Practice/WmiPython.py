from os import supports_bytes_environ
import subprocess
from sys import stderr
p1 = subprocess.run('dir', shell=True, capture_output=True, text=True) #text bring out the original format withtout the decode in the print out statement
#print(p1.stdout)  #decode convert it to a strings decode()

#redirecting the output to a file
#with open("output.txt", "w") as f:
   # p1 = subprocess.run('dir', shell=True, stdout=f, text=True) #text bring out the original format withtout the decode in the print out statement
    

#Capturing an error
#p1 = subprocess.run('dirid', shell=True, stderr=subprocess.DEVNULL, text=True) #text bring out the original format withtout the decode in the print out statement
#print(p1.stderr)  #decode convert it to a strings decode()


#running a command from a file
#p1 = subprocess.run('powershell.exe', 'test.ps1') #text bring out the original format withtout the decode in the print out statement
#print(p1)  #decode convert it to a strings decode()

p4 = subprocess.check_output("Powershell -ExecutionPolicy byPass -Command Get-Process", text=True)
print(p4)