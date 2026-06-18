def f(x: float) -> float:
    return x + 1

def add(x, y):
    """
    Docstring for add
    
    :param x: Description
    :param y: Description
    """
    return x + y

def power(x, y):
    """
    Power
    
    :param x: First parameter
    :param y: power parameter
    :return: x power y
    """
    return x ** y


def toto(a, b=0, c=0):
    pass

result = f(3)
print(result)
print(add(2, 3))
print(power(2, 3))
print(power(x = 2, 
            y = 3))
toto(3, 1)
# add(3, "4")
# result = f("3")

def sum(*kargs):
    total = 0
    for i in kargs:
        total += i
    return total

print(sum(2,4,5,6))


