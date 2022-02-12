#Classes in python are users define object. This are blue print of a future object
#Instances are specific object created from a specific instance of a class
#For Classes, we follow carmel cases
class Dog():
    #when a function is created inside of a class, it is called a method.
    # the __init__ is a special method that will be called upon whenever you are creating the instance of a class
    # self connect to the instance of this class
    # Attributes are charactise of a class

    #CLASS OBJECT ATTRIBUTE. This value remains true for any instance of the class Dog
    species = 'mammal' #Class Obj Attri
    def __init__(self,breed,name,spots): #Constructor of the class
        self.breed = breed
        self.name = name
        
        #Expect a boolean true/False
        self.spots = spots

my_dog = Dog(breed="lab", name="bingo", spots=False)
print(type(my_dog))
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
print(my_dog.species)