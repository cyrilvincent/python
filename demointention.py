import tp4
import math

l1 = [1,9,3,4,3,10,99,8,2,0]
identity = [x for x in l1]
print(identity)
mul2 = [x * 2 for x in l1]
print(mul2)
filter_even = [x for x in l1 if x % 2 == 0]
print(filter_even)
# Comprehension list
res = list(map(lambda x: math.sqrt(x), filter(lambda x : tp4.is_prime(x), l1)))
# <=>
res = [math.sqrt(x) for x in l1 if tp4.is_prime(x)]
print(res)