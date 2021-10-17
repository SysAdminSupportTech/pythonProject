import math
def vol(val):
    """
        This function calc the volume of a spere
    """
    v = 3/4
    pie = math.pi
    r = val^3
    volsphere = v*pie*r
    print(volsphere)
vol(5)