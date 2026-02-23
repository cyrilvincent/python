def add(i, j=0):
    return i + j

# f(x) = x + 1
def f(x):
    return x + 1

def factorielle(n: int) -> int:
    """
    Fonction factorielle
    :param n: argument de la factorielle
    :return: n!
    """
    facto = 1
    for x in range(2, n + 1):
        facto = facto * x
    return facto

result = add(3)
print(result)
print(factorielle(5))
print(f(2))