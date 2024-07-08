import tp_function

def infinite():
    i = 0
    while True:
        i += 1
        yield i

def range(n):
    i = 0
    while i < n:
        yield i
        i += 1

def filter(fn, l):
    for v in l:
        if fn(v):
            yield v # Clone l'interpreteur, pour l'interpreteur 1 = return pour l'interpreteur 2 = j'attends
def map(fn, l):
    for v in l:
        yield fn(v)

if __name__ == '__main__':
    # l = infinite()
    l = range(10)
    res = filter(tp_function.is_prime, l)
    # res = filter(tp_function.is_even, res)
    res = list((x ** 2 for x in res))
    # <=> intention list
    res = map(lambda x: x ** 2, res)
    # print(res[1])
    for v in res:
        print(v)
    for v in res:
        print(v)
