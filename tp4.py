import tp1

l = [1,3,-9,0,99,2,5,7,8,18]

def sum(l):
    res = 0
    for val in l:
        res += val
    return res

def filter2(fn, l):
    res = []
    for val in l:
        if fn(val):
            res.append(val)
    return res

print(sum(l))
print(list(filter(tp1.isEven, l))) # => [0,2,8,18]
print(filter2(lambda x : x % 2 == 0, range(100))) # => [0,2,8,18]
print(filter2(tp1.isPrime, l)) # => [3,2,5,7]
print(filter2(tp1.isPrime, range(100))) # => [3,2,5,7]
# res = filter(tp1.isEven, filter(tp1.isPrime, range(10000000000000000000000)))
# for i in res:
#     print(i)


def map2(fn, l):
    res = []
    for i in l:
        res.append(fn(i))
    return res

print(map2(lambda x: x * 2, l))
print(list(map(lambda x: x * 2 , l)))

resfilter = filter(tp1.isPrime, range(100))
resmap = map(lambda x : x ** 2, resfilter)
print(list(resmap))
print(list(map(lambda x : x ** 2, filter(tp1.isPrime, range(100)))))
#<=> Intention list <=> Comprehension list
print([x ** 2 for x in range(100) if tp1.isPrime(x)])