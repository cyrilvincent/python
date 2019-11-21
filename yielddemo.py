def filter(fn , l):
    for i in l:
        if fn(i):
            yield i

def map(fn, l):
    for i in l:
        yield fn(i)

def list(g):
    res = []
    for i in g:
        res.append(i)
    return res

l = range(1000000000000000000000000000000000000000000000000)
import tp2
res = map(lambda x : x ** 2, l)
res = filter(tp2.isPrime, res)
print(list(res))
res = list(filter(lambda x : x % 2 == 0, res))
print(res)
for i in res:
    print(i)

res = list(filter(lambda x : x % 2 == 0, res))
# <=>
res = [x for x in res if x % 2 == 0]
# <=>
res = list((x for x in res if x % 2 == 0))
