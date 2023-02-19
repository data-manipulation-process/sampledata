fruits = {"apple", "banana", "cherry"}

if "apple" in fruits:
    print("Yes, apple is a fruit")
else:
    print("Yes, not is a fruit")


fruits.add("orange")

print(fruits)

more_fruits = ["orange", "mango", "grapes"]

fruits.update(more_fruits)

print(fruits)

fruits.remove("orange")

print(fruits)

fruits.discard("banana")

print(fruits)