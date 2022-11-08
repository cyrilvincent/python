import tp2
import math

l = [1,5,6,8,9,12,11,15]

# def filter(fn, l):
#     res = []
#     for value in l:
#         if fn(value):
#             res.append(value)
#     return res
#
# def map(fn, l):
#     res = []
#     for value in l:
#         res.append(fn(value))
#     return res

print(filter(lambda x: x % 2 == 0, range(100)))
print(filter(tp2.is_prime, range(100)))
print(filter(lambda x: math.sin(x) > 0, range(100)))
print(map(lambda x: x + 1, range(100)))

# res = filter(tp2.is_prime, filter(lambda x: x % 2 == 0, range(100000000000000000)))
# for i in res:
#     print(i)

res = [x ** 2 for x in range(100)]
print(res)
res = list(map(lambda x: x ** 2, range(100)))
print(res)

res = [x for x in range(100) if x % 2 == 0]
print(res)
res = list(filter(lambda x: x % 2 == 0, range(100)))
print(res)
res = [math.sin(x) for x in range(100) if x % 2 == 0]
print(res)