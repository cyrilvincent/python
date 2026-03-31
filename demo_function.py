def f(x):
    return x + 1  # f(x) = x + 1

def add(x:int , y: int=0) -> int:
    return x + y

def power(x, pow):
    """
    blah blah blah
    :param x: x
    :param pow: la puissance
    :return: x ** y
    """
    return x ** pow

result = f(3)
print(result)
nb = add(2,3.14)
print(nb)

print(add(x=2, y=3))
print(power(pow=3, x=2))
print(add(2))

power(x=2,pow=3)
