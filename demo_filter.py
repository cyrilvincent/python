def is_even(n):
    return n % 2 == 0

def inc(n):
    return n + 1

def complex(n):
    if n % 2 == 0:
        n *= 2
    else:
        n -= 1
    return n

l1 = [0,1,2,99,4,99,6,-2,45,10]

res = list(filter(is_even, l1))
print(res)

res = list(map(inc, l1))
print(res)

res = list(map(complex, l1))
print(res)