def f(x):
    return x + 1

def add(a, b):
    return a + b

def sum(n: int) -> int:
    total = 0
    for i in range(n):
        total += i
    return total

def fake(a, b, c,toto=99, titi=0):
    """
    C'est la fonction fake
    :param a: Le paramètre a
    :param b:
    :param c:
    :param toto:
    :param titi:
    :return: N'importe quoi
    """
    result = a + b * 2 + c - toto + titi
    return result

def is_even(n: int) -> bool:
    if n % 2 == 0:
        return True
    else:
        return False

def is_even2(n: int) -> bool:
    return n % 2 == 0

result = f(3)
print(result)
print(f(3))
result = f(x=3)
print(add(3, 2), add(a=3, b=2), add(b=2, a=3))
print(sum(add(7,3)))
print(fake(1,2,3, titi=1000))
result2 = sum(10)
# Types : str, int, float, bool
print(is_even(7), is_even(8))

