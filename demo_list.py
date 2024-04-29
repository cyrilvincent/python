import hello
import math

def remove_all(l, x):
    nb = l.count(x)
    for _ in range(nb):
        l.remove(x)

def filter_prime(l):
    res = []
    for v in l:
        if hello.is_prime(v):
            res.append(v)
    return res

def filter2(fn, l):
    res = []
    for v in l:
        if fn(v):
            res.append(v)
    return res

def map2(fn, l):
    res = []
    for v in l:
        res.append(fn(v))
    return res

def map_yield(fn, l):
    for v in l:
        yield fn(v)

# f(x) = x + 1
f = lambda x: x + 1
# <=>
def f(x):
    return x + 1

def filter_yield(fn, l):
    for v in l:
        if fn(v):
            yield v

def range_yield(nb):
    i = 0
    while i < nb:
        yield i
        i += 1

def infinite():
    i = 0
    while True:
        yield i
        i += 1



if __name__ == '__main__':
    l = [1, 2, 3, 4, 3, 5, 3, 6, 7]
    remove_all(l, 3)
    print(l)
    print(filter_prime(l))
    print(list(filter(hello.is_prime, l)))
    print(filter2(hello.is_prime, l))
    print(list(map(lambda x: x+1, l)))

    big = infinite() # range(100000000000000000000000000000000000000000000000)
    res = filter_yield(lambda x: x % 2 == 0, big)
    res = filter_yield(lambda x: hello.is_prime(x), res)
    res = map_yield(lambda x: x **2, res)
    for x in res:
        print(x)
