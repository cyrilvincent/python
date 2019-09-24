l = range(100)

def filter(predicateFn, l):
    for i in l:
        if predicateFn(i):
            yield i

def map(mapFn, l):
    for i in l:
        yield mapFn(i)

def list(l):
    res = []
    for i in l:
        res.append(i)
    return res

import tp3
# res = filter(lambda x : tp3.isPrime(x), l)
# res = filter(lambda x : x % 2 == 0, res)
# #
# for i in res:
#     print(i)

res = map(lambda x : x ** 2, filter(lambda x : tp3.isPrime(x), l))
for i in res:
    print(i)
