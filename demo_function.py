def add(i: float, j:float =0) -> float:
    """
    Add 2 numbers
    :param i: first param
    :param j: second param
    :return: i + j
    """
    return i + j


res = add(2,3)
res = add(i=2, j=3)
res = add(1)
print(res)

# f(x) = x + 1
def f(x):
    return x + 1

print(f(1))