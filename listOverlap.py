import random
a = [random.randrange(1, 10, 1) for i in range(random.randint(1, 20))]
b = [random.randrange(1, 10, 1) for e in range(random.randint(1, 20))]
print(set([i for i in a and b if i in a and b]))