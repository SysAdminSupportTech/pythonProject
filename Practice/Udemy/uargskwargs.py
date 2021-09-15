"""
def myfunc(a,b):
    # return 5% of the sum of a and b
    return sum((a,b)) * 0.05
print(myfunc(10,20))
"""

#Using the *args function
def myfunc(*args):
    # return 5% of the sum of a and b
    return sum(args) * 0.05
    # Note: args is an arbitary value. any word can replace the value and you still get the same output.
#print(myfunc(2,3,4,5,6,7,45,3,4,56))


#Building a key word argument using **kwargs. Note this create a dictionary
def myfunc2(**kwargs):
    if 'fruit' in kwargs:
        print('my fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I dont find a fruit of your choice here.')
#print(myfunc2(fruit='apple'))

def myfunct(*args):
    nums=[]
    for item in args:
        if item % 2 == 0:
            nums.append(item)
        else:
            pass
    return nums
#print(myfunct(2,3,4,5,6,7,8))

#This convert all even numbers in letter into small letters
def myfunc3(x):
    out = []
    for i in range(len(x)):
        if i % 2 == 0:
            out.append(x[i].lower())
        else:
            out.append(x[i].upper())
    return ''.join(out)
print(myfunc3('alberteromosele'))