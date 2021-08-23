#importing os module
import os

#Navigating the root directory
path = "/"
dir_path = os.listdir(path)
print("Files and Directories in '", path, "' :")

print(dir_path)