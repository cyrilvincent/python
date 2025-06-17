import math

l = range(100)
result = [math.sqrt(x * 2) for x in l] # Map
print(result)

result = [x for x in l if x % 2 == 0] # Filter
print(result)

result = [math.cos(x) for x in l if x % 2 == 0] # Filter + Map
print(result)

result2 = [x ** 2 for x in result]
print(result)


# def double(l: list[float]) -> list[float]:
#     result=[]
#     for value in l:
#         result.append(value * 2)
#     return result
#
# if __name__ == '__main__':
#     print(double(l))