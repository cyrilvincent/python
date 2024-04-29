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

# f(x) = x + 1
f = lambda x: x + 1
# <=>
def f(x):
    return x + 1



if __name__ == '__main__':
    l = [1, 2, 3, 4, 3, 5, 3, 6, 7]
    remove_all(l, 3)
    print(l)
    print(filter_prime(l))
    print(list(filter(hello.is_prime, l)))
    print(filter2(hello.is_prime, l))
    print(list(map(lambda x: x+1, l)))

    big = range(100000000000000000000000000000000000000000000000)
    res = filter(lambda x: x % 2 == 0, big)
    res = filter(lambda x: hello.is_prime(x), res)
    for x in res:
        print(x)
