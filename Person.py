"""
What is inheritance?
#Using the attributes and methods from one class in another class
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

#Enemy class inherit Person class
#super() keyword used to implement inheritance
class Enemy(Person):
    def __init__(self, weapon, fname, lname, health, status):
        super().__init__(fname,lname,health,status)
        self.weapon = weapon

    def hurt(self, other):
        if self.weapon == "rock":
            other.health -= 10
        elif self.weapon == "stick":
            other.health -= 5
        print(other.health)

    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak ".format(other.fname))

    def steal(self, other):
        print(("ha ha ha, I have your stuff! "))

Alex = Enemy("rock", "alex", "wayne", 55,status = False)
Alex.hurt(Kranthi)
Alex.hurt(Kranthi)
Alex.hurt(Kranthi)
Alex.insult(Kranthi)
Alex.steal(Kranthi)
Alex.steal(Kumar)
Alex.steal(Panda)

