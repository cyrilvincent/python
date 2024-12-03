def identity(x):
    return x

def increment(x):
    return x + 1


def max(a=0, b=0):
    """
    maximum of 2 number
    :param a: first param
    :param b: second param
    :return: max of a and b
    """
    if a > b:
        return a
    else:
        return b

result = increment(3)
print(result)
print(max(2,3))
max(a=2,
    b=3)
max(2,3)
