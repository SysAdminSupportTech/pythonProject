class Circle():
    #CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius*radius*Circle.pi

    #method
    def get_circumference(self):
        return self.radius * self.pi * 2
my_circle = Circle()
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.area)
print(my_circle.get_circumference())
