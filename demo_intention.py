import math

import tp_function

l = [1,2,3,55,99,-2,4,8,-3,1000]

double = [x * 2 for x in l]
print(double)

sin = [math.sin(x) for x in l]
print(sin)

filter_even = [x ** 2 for x in l if x % 2 == 0]
print(filter_even)


def complex_function(x: float) -> float:
    if x % 2 == 0:
        return x ** 2
    else:
        return x / 2


ifelse = [x ** 2 if x % 2 == 0 else x / 2 for x in l]
print(ifelse)

ifelse = [complex_function(x) for x in l]
print(ifelse)

primes = [x for x in range(100) if tp_function.is_prime(x)]
print(primes)

complex = [complex_function(x) for x in l if tp_function.is_prime(x)]
