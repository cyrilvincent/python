def f():
    return 1

def g(x):
    return x + 1

def h(x, y):
    """
    blah blah
    :param x: param1
    :param y: param2
    :return: x+y
    """
    return x + y

def add(x: float,y: float=0) -> float:
    return x + y

res = f()
print(res)

res = g(1)
print(res)
print(g(1))

print(h(3,2))
print(h(x=3, y=2))

print(add(2,3))
print(add(2,3))

h(3,2)
