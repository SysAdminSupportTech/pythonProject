import os

directory = 'Geeksforgeeks'

Parent = os.getcwd()

#path
path = os.path.join(Parent, directory)
os.removedirs(path)
