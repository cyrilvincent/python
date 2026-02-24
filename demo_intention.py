import math
import demo_function

l = [1, 99, 50, -1, 23, 45, 7, 11, 9, 10]

# result=[]
# for v in l:
#     result.append(v ** 2)
# print(result)

result = [math.sin(x) for x in l]
print(result)

result = [x for x in l if x % 2 == 0]
print(result)

result = [math.sin(x) for x in l if x % 2 == 0]
print(result)

result = [math.sin(x) for x in l if demo_function.is_prime(x)]
print(result)