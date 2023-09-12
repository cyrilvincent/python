import math
import my_module

l1 = [1,2,38,99,7,99,25,57]
result = [x for x in l1]
print(result)

result = [x + 1 for x in l1]
print(result)

result = [x ** 2 for x in l1]
print(result)

result = [math.sin(x) for x in l1]
print(result)

result = [x for x in l1 if x % 2 == 0 and x > 3]
print(result)

result = [x for x in l1 if math.sin(x) > 0]
print(result)

result = [x for x in l1 if my_module.is_prime(x)]
print(result)

result = [x ** 2 for x in l1 if my_module.is_prime(x)]
print(result)
