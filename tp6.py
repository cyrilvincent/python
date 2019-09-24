l = [2,10,5,1]
print(l[1])
l.append(99)
for v in l:
    print(v)
print(l[1:-1])
print(l.index(5))
print(55 in l)

l = [1,2,3,4,5,3,4,3,0]
print(l)
for i in range(l.count(3)):
    l.remove(3)
print(l)

l = range(1000)

def filterEven(l, predicatFn):
    res = []
    for i in l:
        if predicatFn(i):
            res.append(i)
    return res

import math
def debile(x):
    return x % 3 == 0 and math.sin(x) > 0

import tp3
print(filterEven(l, debile ))

res = list(filter(tp3.isEven, l))
print(res)

res = list(filter(tp3.isPrime, l))
print(res)

res = list(filter(lambda x : tp3.isPrime(x), l))
print(res)

def mymap(mapFn, l):
    res = []
    for i in l:
        res.append(mapFn(i))
    return res

l = range(100000000000000000000000000)

res = map(lambda x : x ** 2, filter(tp3.isPrime, l))
#res = filter(lambda x : x % 2 == 0, filter(tp3.isPrime, l))
#print(res)
for i in res:
    print(i)


res = list(map(lambda x : x ** 2, filter(lambda x : tp3.isPrime(x), l)))
#<=> Intention List
res = [x ** 2 for x in l if tp3.isPrime(x)]

res = map(lambda x : x ** 2, filter(lambda x : tp3.isPrime(x), l))
#<=> Generator
res = (x ** 2 for x in l if tp3.isPrime(x))






