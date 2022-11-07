z = "global"

def add(x: float, y: float, *kargs, **kwargs) -> float:
    sum = x + y
    for i in kargs:
        sum += i
    if "toto" in kwargs:
        print(kwargs["toto"])
    return sum

print(add(2,3,4, toto=5))
print(add(y=3, x=2))
print(add(2, y=3))
print(add(2,3))

def add2(*x):
    sum = 0
    for i in x:
        sum += i
    return sum

print(add2())

toto = add
print(toto(2,3))

# f(x) = x + 1
def f(x):
    return x + 1

f = lambda x : x + 1
print(f(3))