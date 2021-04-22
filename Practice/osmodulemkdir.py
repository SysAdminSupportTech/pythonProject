import os
#Creating a directory Name
directory = "GeeksforGeeks"

#parent Directory
parent_dir = os.getcwd()

#Creating a directory
path = os.path.join(parent_dir, directory)

print(path)

os.mkdir(path)
print("Directory '% s' created" % directory)