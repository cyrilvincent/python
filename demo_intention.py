import tp4

l = range(100)
res = [x ** 2 for x in l]
print(res)
res = [x for x in l if x % 2 == 0]
print(res)
res = [x ** 2 for x in l if x % 2 == 0]
print(res)
res = [x ** 2 for x in l if tp4.is_prime(x)]
print(res)