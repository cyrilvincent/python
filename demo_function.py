def f(x):
    return x + 1

def add(a: int, b: int=0):
    return a + b

result = f(5)
print(result)
print(f(5))
print(add(3))
add(a=2,b=3)
