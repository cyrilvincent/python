def add(a: float, b:float = 0.0) -> float:
    y  = a + b
    return y

def sqrt(x):
    return x ** 0.5

a = 1
b = 2
y = add(a, b)
print(y)
print(add(1,2))
add(b = 2, a = 3)
add(1)
add(3.14,2.2)
add("toto")
z:int = 3
