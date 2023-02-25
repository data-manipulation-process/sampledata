def my_function():
    print("Hello from a fuction")

my_function()

def my_function(fname, lname):
    print(fname, lname)

def my_function(x):
    return x + 5

def my_fuction(*kids):
    print("The youngest child is " + kids[2])

def my_function5(**kid):
    print("His last name is " + kid["lname"])

def my_function5(fname, lname):
    print(fname, lname)

my_function5("Jagan", "Naidu")

x = lambda a:a

print(x(10))