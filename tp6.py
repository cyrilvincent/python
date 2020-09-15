import libs.tp3 as mylib

l = range(10)

res= []
for val in l:
    res.append(val ** 2)

print(res)

print(list(map(lambda x : x **2, l)))

intention = [x ** 2 for x in l]
print(intention)

print(list(filter(lambda x : x % 2 == 0, l)))
intention = [x for x in l if x % 2 == 0]
print(intention)

print(list(map(lambda x : x ** 2, filter(lambda x : x % 2 == 0, l))))
intention = [x ** 2 for x in l if x % 2 == 0]
print(intention)


intention = [x ** 2 for x in l if mylib.is_prime(x)]
print(intention)