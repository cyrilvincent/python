import tp_function

l = range(1000000000000000000000000000000000000000000000000000000000000000000000000000000)
res = (x for x in l if tp_function.is_prime(x))
res = (x ** 2 for x in res if tp_function.is_even(x))
for v in res:
    print(v)