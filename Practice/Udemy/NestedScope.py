#LEGB format for variable scope
#Local
#Enclosing function Local
#Global
#Buildin

x = 25
def printer():
    x = 50
    return x
print(x)
print(printer())