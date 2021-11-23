import random

x = [random.randint(0, 10) for i in range(10)]
print(x)
print("число 5 находится в списке под номером", x.index(5)+1)
