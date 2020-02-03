import tp1

def filter2(fn, l):
    for val in l:
        if fn(val):
            yield val

def map2(fn , l):
    for val in l:
        yield fn(val)

def range2(nb):
    i = 0
    while i<nb:
        yield i
        i+=1

def infiniteLoop():
    i = 0
    while(True):
        yield i
        i += 1

def list2(l):
    res = []
    for i in l:
        res.append(i)
    return res

res = filter2(tp1.isPrime, range2(100))
res = filter2(tp1.isEven, res)
res = map2(lambda x : x ** 2, res)
for i in res:
    print(i)