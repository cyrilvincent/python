import math
import my_lib

l = [1,2,3,4,5,6,7,8,9,0]

# identité
res = [x for x in l]
print(res)

# map
res = [x + 1 for x in l]
print(res)

res = [math.cos(math.tanh(x * 0.5)) for x in l]
print(res)

# filter
res = [x for x in l if x % 2 == 0]
print(res)

# filter + map
res = [x ** 2 for x in l if my_lib.is_prime(x)]
print(res)