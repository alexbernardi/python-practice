num = int(input("enter a number"))
div = [i for i in range(1, num + 1) if num % i == 0]
print(div)
