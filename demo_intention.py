import math
import tp_function

l = [1, 2, 3, 8, 9, 1, 99, 0, 66, 88]

identity = [v for v in l]
print(identity)

# Map
double = [v * 2 for v in l]
print(double)

# Filter
even = [v for v in l if v % 2 == 0]
print(even)

even_double = [v * 2 for v in l if v % 2 == 0]
print(even_double)

even_double_or_sqrt = [v * 2 if v % 2 == 0 else math.sqrt(v) for v in l]
print(even_double_or_sqrt)

result = [math.tanh(v) for v in l if tp_function.is_prime(v)]
print(result)