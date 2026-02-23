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

def is_prime(n: int) -> bool:
    """
    Calcul si n est un nombre premier
    :param n: n
    :return: True si n est premier
    """
    is_prime = True
    for div in range(2, int(n ** 0.5) + 1):
        if n % div == 0:
            is_prime = False
            break
    return is_prime

def sin():
    return "toto"

if __name__ == '__main__':
    result = add(3)
    print(result)
    print(factorielle(5))
    print(f(2))
    print(is_prime(7))