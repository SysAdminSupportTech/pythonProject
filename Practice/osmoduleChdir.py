import os
def current_path():
    print("Current Working Directory Before")
    print(os.getcwd())
    print()
current_path()

os.chdir('../../')

current_path()