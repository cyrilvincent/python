import math
import my_package.tp_function as tp

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def f(x):
    return math.sin(x / 100) + 1

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

identity = [x for x in l]
print(identity)

increment = [x + 1 for x in l]
print(increment)

sin_list = [math.sin(x) for x in l]
print(sin_list)

flist = [f(x) for x in l]
print(flist)

filter_list = [x for x in l if x % 2 == 0]
print(filter_list)

filter2_list = [x * 2 for x in l if x % 2 == 0]
print(filter2_list)

f2_list = [f(x) for x in l if is_even(x)]
print(filter2_list)

# TP Filtrer les nombres premiers et les monter au carré **
result = [x ** 2 for x in l if tp.is_prime(x)]
print(result)
