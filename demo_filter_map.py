import tp3

l = [1,2,5,9,99,-1,0,8,14,50]

res = filter(tp3.is_prime, l)
print(list(res))

def inc(x):
    return x + 1

def double(x):
    return x * 2

res = map(double, l)
print(list(res))

res = map(lambda x: x * 2, l)
print(list(res))
