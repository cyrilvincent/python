def add(a: int, b=0.):
    """
    Add 2 numbers
    :param a: first number
    :param b: second number
    :return: a+b
    """
    return a + b

def add2(*kargs):
    total = 0
    for arg in kargs:
        total += arg
    return total

result = add(3,2)
print(result)
print(add(3,2))
print(add(b=2, a=3))
print(add2())
print(add2(3))
print(add2(2,3))
print(add2(1,2,3,4,5,6,7,8,9))




