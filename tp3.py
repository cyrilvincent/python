# Créer les fonction fact(n: int) -> int et is_prime(n: int) -> bool

def fact(n: int) -> int:
    """
    Factorielle
    :param n: entier
    :return: n!
    """
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def is_prime(n: int) -> bool:
    """
    Prime number
    :param n: param
    :return: true if n is prime
    """
    if n < 2:
        return False
    for div in range(2, n):
        if n % div == 0:
            return False
    return True

def sin(x):
    return "toto"


if __name__ == '__main__':
    print(fact(5))
    print(is_prime(7919))