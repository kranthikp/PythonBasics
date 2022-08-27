"""
multiple inheritance
#when one class inherits from multiple classes,
and is able to use attributes and methods from both classes

pros # ability to resuse small amounts of code in multiple classes
cons # order of inheritance matters, no of classes, common methods etc

implent multiple inheritance in two ways -
1. non pythonic - requires maintainance
2. using super() method
class Animal():
    def __init__(self, sound, look):
    ....

class Place():
    def __init__(self, climate, lat, long):
    ....

class Mammal(Animal, Place):
    def __init__(self, sound, look,lat, long, food):
        Animal.__init__(self, sound, look)
        Place.__init__(self, climate, lat, long)
        self.food = food
"""

#Parent class 1
class Items():
    def __init__(self, sku):
        self.sku = sku

    def print_sku(self):
        print("The sku is {}".format(self.sku))

#Parent class 2
class Garment():
    def __init__(self, section, type):
        self.section = section
        self.type = type

    def print_garment(self):
        print("The garment is in section {}, {}.".format(self.section, self.type))

# Child class
class Shirts(Items, Garment):
    def __init__(self, sku, section, type, name, color):
        self.name = name
        self.color = color
        Items.__init__(self, sku)
        Garment.__init__(self, section, type)

    def print_shirt(self):
        print("{} {} on sale!".format(self.color, self.name))

Blouse = Shirts("0001", 43, "tops", "Formal Blouse", "white")

Blouse.print_sku()
Blouse.print_shirt()
Blouse.print_garment()

