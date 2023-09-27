import tp_function

def square(n):
    return n ** 2

l1 = [0,1,2,7,5,99,6,-2,11,10]
# Filtrer par nombre premier et les mettre au carré

res = list(filter(tp_function.is_prime, l1))
print(res)
res = list(map(square, res))
print(res)

print(list(map(square, filter(tp_function.is_prime, l1))))
