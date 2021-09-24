#installing WMI. python.exe -m pip install wmi
#conn = wmi.WMI("13.76.128.231", user=r"prateek", password="P@ssw0rd@123") Connecting to a remote computer
import wmi
import win32api
import os

#After installation of wmi on your computer, the next step is to establish connection
conn = wmi.WMI()

#Getting all the classes in my pyton wmi

def wmi_classes(): #this print all the classes in my wmi object
   for class_name in conn.classes: 
      print(class_name)

def wmi_search_proc():
   for class_name in conn.classes:
      if 'Process' in class_name:
         print(class_name)
#wmi_search_proc()


#Getting all the properties of a specific Method
def class_prop():
   conn.Win32_Process.methods.keys() #getting all methods
   conn.Win32_Process.properties.keys() #Retrieves all properties

#print(class_prop)

#Handling Processes now
def hprocess():
   for process in conn.Win32_process():
      print("ID: {}\nHandleCount: {}\nProcessName: {}\n".format(process.ProcessID, process.HandleCount,process.Name))

#print(hprocess())

#Filter the process
def fprocess():
   for process in conn.Win32_Process(name="python.exe"):
      print("ProcessName: {}, ID: {}".format(process.Name, process.ProcessID))
#print(fprocess())

def biosproc():
   for process in conn.win32_Bios():
      print(process)
#biosproc()

def usrgroup():
   for usr in conn.win32_group():
      print(usr.Caption)
#usrgroup()


def cprocId():
   for proc in conn.win32_process(name="python.exe"):
      print("ID: {}".format(proc.ProcessID))
      print("osCurrendId:", os.getpid())
      print("CurrentID: ", win32api.GetCurrentProcessId())
cprocId()