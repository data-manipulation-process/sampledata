# define Person class
class Person:
    age = 23
    name = "Adam"


# format age
print("{p.name}'s age is: {p.age}".format(p=Person()))


class Person2:
    age = 40
    name = "Jagan"


print("{p.name}'s age is: {p.age}".format(p=Person2()))
