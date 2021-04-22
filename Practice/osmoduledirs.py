import os
#Directory name
directory = "Nikhil"

#Parent Direcory
parent_dir = os.getcwd()

#path
path = os.path.join(parent_dir, directory)

#creating directory
os.makedirs(path)
print("Directory '% s' Created" % directory)
