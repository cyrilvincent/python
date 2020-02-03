import tp1

l = [1,3,-9,0,99,2,5,7,8,18]

def sum(l):
    res = 0
    for val in l:
        res += val
    return res

def filter(fn, l):
    res = []
    for val in l:
        if fn(val):
            res.append(val)
    return res

print(sum(l))
print(filter(tp1.isEven, l)) # => [0,2,8,18]
print(filter(tp1.isEven, range(100))) # => [0,2,8,18]
print(filter(tp1.isPrime, l)) # => [3,2,5,7]
print(filter(tp1.isPrime, range(100))) # => [3,2,5,7]
print(filter(tp1.isEven, filter(tp1.isPrime, range(100))))# => [2]