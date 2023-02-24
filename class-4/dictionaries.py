car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


print(car.get("model"))

car["year"] = 2020
car["color"] = "red"

print(car)
print("22222222")
car.pop("model")
print(car)

print("3333333333")
car.clear()


"""
pop - to remove the element 
clear - to clear all elements
"""
