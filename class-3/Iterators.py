
mytuple = ("apple", "Banana", "cherry")

myit = iter(mytuple)

print(next(myit, 3))

# for i in myit:
#     print(i)


for i in myit:
    print(i)

for i, name in enumerate(mytuple):
    print(i, name)

"""
"""
class MyNumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumber()
myiter = iter(myclass)

for x in myiter:
    print(x)