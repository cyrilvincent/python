import math
import tp_function

l = [1,2,3,4,5,6,7,8,9,10]

res = []
for value in l:
    res.append(value * 2)

print(res)

# Intention, map
res = [x * 2 for x in l]
print(res)

# Intention, filter
res = [x for x in l if x % 2 == 0]
print(res)

# Intention
res = [tp_function.is_prime(x) for x in l if x % 2 == 0]
print(res)

# TP
# Filtrer les nombres premiers < 100 et les monter au carré
# Filtrer les nombres premiers pairs
# Filtrer les nombres premiers se terminant par 3
l = list(range(100))
print([x ** 2 for x in l if tp_function.is_prime(x)])
print([x for x in l if tp_function.is_prime(x) and x % 2 == 0])
print([x for x in l if tp_function.is_prime(x) and x % 10 == 3])