num = 101

flag = False

if num == 1:
    print(num, " is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num % i)
            flag = True
            break
    if flag:
        print(num, "is not a prime number ")
    else:
        print(num, "is a prime number")
#


if num == 1:
    print(num, " is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            break
            print(num, "is not a prime number")

    else:
        print(num, "is prime number")

else:
    print(num, "is not a prime number")


