"""
Inhertance

"""

class Person:
    def __init__(self, name, age):
        self.fname = name
        self.age = age
    def printname(self):
        print(self.fname)
    def printage(self):
        print(self.age)

class Student(Person):
    pass

x1 = Student("Jagan",11)

x1.printname()
x1.printage()