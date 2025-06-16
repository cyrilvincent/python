def add(a: int, b=0.):
    """
    Add 2 numbers
    :param a: first number
    :param b: second number
    :return: a+b
    """
    return a + b

result = add(3,2)
print(result)
print(add(3,2))
print(add(b=2, a=3))
add("toto")




