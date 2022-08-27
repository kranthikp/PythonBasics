"""
Classes
#allows to group data and info like var and functions
into single organaized unit

single file per class
OR
Multiple classes can be contained in one file

#inheritance
derived/child class can use attributes and methods of parent class

#multiple inheritance
derived/child class can inherit attributes and methods from more than one lass

#polymorphism
derived/child classes can override class mthods of parent class

#all classes in python are objects
#Class variables: for use by all the methods in the class
#Instance variables: for use by specific method in which yhe variable
is declared/created

#__init__method : sets attributes for an object at object creation; is a constructor**
its the first method of the class{predetermined}

**the word constructor is another word that can be ised to refer
to the __init__method

#self : an instance of a class, and references the obj that is constructed by the init method

#to define class is keyword
class <className>:
"""
import random

class Person:
    def __init__(self, fname, lname, health, status):
        "initialzie attricbutes to be ised in/available for all \
        methods in this class, and for class objects created \
        by this class."
        self.fname =fname
        self.lname = lname
        self.health = health
        self.status = status

    def introduce(self):
        "All people introduce themselves"
        print("hello, my name is {} {}".format(self.fname,self.lname))

    def emote(self):
        emotion =random.randrange(1,3)
        if emotion == 1:
            print("{} is happy today".format(self.fname))
        elif emotion ==2:
            print("{} is sad today".format(self.fname))

    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy!".format(self.fname))
        elif self.health >= 76:
            print("{} is little tired today!".format(self.fname))
        elif self.health >= 51:
            print("{} is feels unwell!".format(self.fname))
        elif self.health >= 40:
            print("{} goes to doctor!".format(self.fname))
        else:
            print("{} is unconscious!".format(self.fname))

#initialize instance with values
Kranthi = Person("Kranthi", "panda", 95, status=True)
Kumar = Person("Kumar", "panda", 55, status=True)
Panda = Person("KK", "panda", 33, status=True)

print("{} is my Friend? {}".format(Kranthi.fname, Kranthi.health))
print("{} is my Friend? {}".format(Panda.fname, Panda.health))

Kranthi.introduce()
Kumar.introduce()
Panda.introduce()

Kranthi.status_change()
Kumar.status_change()
Panda.status_change()