#Intention list
import math

l = [1, 2, 5, 99, 10, -1, 0, 99, 88, 41]

def f(x):
    return x * math.sin(x)

def g(x):
    if x % 2 == 0:
        return x * 2
    else:
        return x - 1

result = [f(x) for x in l if x % 2 == 0] # identity
print(result)

result = [x * 2 if x % 2 == 0 else x - 1 for x in l]
print(result)

result = [g(x) for x in l]
print(result)