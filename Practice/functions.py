import math
def f():
    pass

def ping():
    return "Ping!"
ping()

def volume(r):
    """ Return the volume of a sphere with radius r."""
    v = (4.0/3.0) * math.pi * r**3
    return v

print(volume(2))

#Keyword Argument
def cm(feet = 0, inches=0):
    """Convert a lenght from feet and inches to centimeters."""
    inches_to_cm = inches * 2.54
    feet_to_cm = feet *12 * 2.54
    return inches_to_cm + feet_to_cm

print(cm(feet = 5))
print(cm(inches= 78))