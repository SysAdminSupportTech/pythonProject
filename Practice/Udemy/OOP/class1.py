#Class with Attribute
class Computer(): #this is my class name
    def __init__(self,screen,color,ram,hdd,hddSize,processor):
        self.screen = screen
        self.color = color
        self.ram = ram
        self.hdd = hdd #Hard disk type (SATA or HDD)
        self.processor = processor #Processor type(intel or AMD)
        self.hddSize = hddSize

laptop = Computer(hdd="SATA", hddSize="500 GB", color="Black", ram=4,processor="Intel",screen="15 inch") #Creating an instance of my class
print(laptop.hdd)
print(laptop.hddSize)
print(laptop.color)
laptop.ram
laptop.processor
laptop.screen
