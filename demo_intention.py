import math
import tp_function

l = [1,2,5,9,15,-2,0,88]

double = [x * 2 for x in l]
print(double)

evens = [x for x in l if x % 2 == 0]
print(evens)

evens_double = [x * 2 for x in l if x % 2 == 0]
print(evens_double)

result = [math.sqrt(x) for x in l if tp_function.is_prime(x)]