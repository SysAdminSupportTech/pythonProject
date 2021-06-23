import os
#basedir = os.path.expanduser('~')
#for entry in os.listdir(basedir):
   # if os.path.isdir(os.path.join(basedir, entry)):
       # print(entry)

#using scandir
basedir = os.path.expanduser("~")
with os.scandir(basedir) as entries:
    for entry in entries:
        print(entry.name)