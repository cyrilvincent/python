def add(x, y=0.0):
    """
    Add 2 numbers
    :param x: 1st number
    :param y: 2nd number
    :return: x+y
    """
    return x + y


result = add(2,3.14)
print(result)

result = add(y=3, x=2)
print(result)

result = add(3)
print(result)



