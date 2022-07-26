number = int(input("enter a number in integer form: "))
if number % 4 == 0:
    print("your number was divisible by 4")
elif number % 2 == 0:
    print("your number was even")
else:
    print("your number was odd")
num = int(input("enter a number to be divided: "))
check = int(input("enter a number to divide the previously entered number: "))
if (num / check) % 2 == 0:
    print("the divided number is even")
else:
    print("your number was odd")
