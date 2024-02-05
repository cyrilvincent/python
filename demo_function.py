def add(i:float, j:float=0) -> float:
    """
    Sum
    :param i: first param
    :param j: second argument
    :return: i+j
    """
    return i + j

res = add(2, 1)

print(res)

def add_tuple(*args):
    res = 0
    for arg in args:
        res += arg
    return res

print(add_tuple())
