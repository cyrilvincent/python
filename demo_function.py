def add(a: float, b: float=0) -> float:
    """
    Add 2 numbers
    :param a: first param
    :param b: second param
    :return: a+b
    """
    return a + b

result = add(1,2)
add(1)

print(result)
print(add(result,5))
print(add(2,3))

# Mauvaise pratique, il faudrait avoir un return
# def add2(a, b):
#     print(a+b)
# add2(2,3)

# TP : Créer la fonction is_prime(n:int) -> bool

