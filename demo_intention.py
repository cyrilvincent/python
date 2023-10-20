import tp_function
import math

def my_function(x):
    return math.sin(2 * x / 10)


l1 = [1, 2, 4, 99, 13, -2, 99, 48, 22, 10]


res = [x for x in l1 if tp_function.is_prime(x)]
res = [x ** 2 for x in res if tp_function.is_even(x)]
print(res)

l2 = range(100000000000000000000000000000000000000000000000000000000)
res = (x for x in l2 if tp_function.is_prime(x))
# res = (x for x in res if tp_function.is_even(x))
for x in res:
    print(x)