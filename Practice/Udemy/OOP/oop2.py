#Classes in python are users define object. This are blue print of a future object
#Instances are specific object created from a specific instance of a class
#For Classes, we follow carmel cases
#
class Dog():
    #CLASS OBJECT ATTRIBUTE. This value remains true for any instance of the class Dog
    species = 'mammal' #Class Obj Attri

    #This is a user define attribute
    def __init__(self,breed,name): #Constructor of the class
        self.breed = breed
        self.name = name

    #Methods are function acting on an object.
    #Methods are function inside a class
    #OPERATIONS/Action -----> Methods
    #Method usually information about the object it self.
    #Method can take other arguments
    #Number is not reference with self.number because is not referencing any instance of a class, but a value provided by the user when the method is called
    
    def bark(self,number):
        print("WOOF ! My name is {}, and my number is {}".format(self.name, number))


my_dog = Dog(breed="lab", name="bingo")
print(my_dog.breed)
print(my_dog.name)
print(my_dog.species)

print(my_dog.bark(20))



#attributes are just information about a given class