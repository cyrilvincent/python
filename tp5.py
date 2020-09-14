import libs.tp3 as mylib

l = [1,2,5,99,8,54,53,6,7,98]

def filter_even(l):
    res = []
    for val in l:
        if mylib.is_even(val):
            res.append(val)
    return res

def filter_prime(l):
    res = []
    for val in l:
        if mylib.is_prime(val):
            res.append(val)
    return res

def filter_generic(fn, l):
    res = []
    for val in l:
        if fn(val):
            res.append(val)
    return res

print(filter_even(l))
print(filter_prime(l))
print(filter_generic(mylib.is_even, l))
print(filter_generic(mylib.is_prime, l))
print(list(filter(mylib.is_even, l)))
print(list(filter(mylib.is_prime, l)))
print(list(filter(lambda x : x % 2 == 0, l)))
print(list(filter(lambda x : mylib.is_prime(x) == 0, l)))

def inc(l):
    res = []
    for val in l:
        res.append(val + 1)
    return res

def square(l):
    res = []
    for val in l:
        res.append(val ** 2)
    return res

print(inc(l))
print(square(l))

def map_generic(fn, l):
    res = []
    for val in l:
        res.append(fn(val))
    return res

print(list(map(lambda x : x ** 2, l)))

res = filter(lambda x : mylib.is_prime(x), l)
print(list(map(lambda x : x ** 2, res)))

print(list(map(lambda x : x ** 2, filter(lambda x : mylib.is_prime(x), l))))


# Créer map_generic
# Tester map : afficher les carrés de la liste
# Tester map + filter : afficher les carrés des nombres premiers de la liste
