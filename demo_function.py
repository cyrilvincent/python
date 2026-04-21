# f(x) = x + 1

def f(x):
    return x + 1

result = f(3)
print(result)
print(f(result))

print(f(3))

def sum(a: int, b: int=0) -> int:
    """
    Somme 2 entier (PyDoc)
    :param a: 1er entier
    :param b: 2ème entier
    :return: a+b
    """
    return a + b

def factorielle(n: int) -> int:
    pass

def is_prime(n: int) -> bool:
    pass

print(sum(3.14,2))
print(sum(a=3, b=2))
print(sum(3))
result = sum(3,2)
sum(a=3)

