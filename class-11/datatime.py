import datetime

# get current datetime
now = datetime.datetime.now()
print(now)

my_list = [10, 20, 'Jessa', 12.50, 'Emma']

print(my_list[-1])
print(my_list[-2])
print(my_list[-3])
print(my_list[-4])
print(my_list[-5])
print()
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])

print(my_list[0:-4])

print()
for item in my_list:
    print(item)

print()
for i in range(0, len(my_list)):
    print(my_list[i])

print()
my_list.append("Jagan")
print(my_list)
my_list.append([25, 50, 75])
my_list.extend([25, 50, 75])
print(my_list)

print()
