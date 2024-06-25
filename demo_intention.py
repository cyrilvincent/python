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
# Filtrer les nombre premiers < 100 et les monter au carré
# Filtrer les nombre premiers pairs
# Filtrer les nombre premiers multiples de 3