# f(x) = x + 1

# f(x) = 3
def f(x):
    return x + 1

def g():
    return 3

def display(x):
    print(x)


def add(x, y):
    return x + y


def add3(x: float, y: float=0, z: float=0) -> float:
    """
    My beautiful function
    :param x: param1
    :param y: param2
    :param z: param3
    :return: sum of x y z
    """
    return x + y + z


def is_prime(n: int) -> bool:
    pass


add3()

add3(3.14)
print(f(3))
result = f(3)
print(result)
add(2, 3)
add(x=2, y=3)
add(y=3, x=2)
add(2, y=3)

add3(1,2,3)
add3(x=1, y=2, z=3)

add3(1,2)
add3(x=1, y=2)

result2 = add3(1, z=3)


