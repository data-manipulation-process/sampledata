year = 2020

if (year % 400 == 0) and (year % 100 == 0):
    print(year % 400)
    print(year % 100)
    print("{0} is a leap yar".format(year))
elif (year % 4 == 0) and (year % 100 != 0):
    print(year % 4)
    print(year % 100)
    print("{0} is a leap year".format(year))
else:
    print(year % 400)
    print(year % 100)
    print(year % 4)
    print("{0} is not leap year".format(year))

