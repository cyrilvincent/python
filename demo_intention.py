import math
import tp_function as tp

l1 = [13,7,77,5,-2,58,99]

# Transformation
result = [math.sin(x) for x in l1]
print(result)

# Filtre
result = [x for x in l1 if x < 50]
print(result)

result = [x for x in l1 if x % 2 == 0]
print(result)

# Filtre + Transformation
result = [x ** 2 for x in l1 if x % 2 == 0]
print(result)


def is_even(x):
    return x % 2 == 0

# Filtre + Transfomation + Fonction
result = [math.sin(x) for x in l1 if tp.is_prime(x)]
print(result)