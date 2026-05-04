for v in range(20, 10, -2):
    toto=3
    print(toto)
    print(v)



def add(i: int, j: int) -> int:
    """
    Doc embarquée
    :param i: param i
    :param j: param j
    :return:  i + j
    """
    return i + j


add2 = lambda i, j: i + j


def sum(*kargs):
    total = 0
    for k in kargs:
        total += k
    return total


result = add(3.14, 2)
add(i=1,j = 2)
print(result)

print(sum(1,2,3,4,5,6))



