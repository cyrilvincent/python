# faire la fonction power(x, y) => x ** y
# Faire la fonction facto(n: int) -> int
# Faire la fonction is_prime(n: int) -> bool
# Bonus faire la fonction qui affiche tous les nb premiers < 1000

def power(x: float, y: float) -> float:
    """
    Power of
    :param x: x
    :param y: y
    :return: x ** y
    """
    return x ** y


def facto(n: int) -> int:
    """
    Factorielle
    :param n:
    :return: n!
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n: int) -> bool:
    """
    Return true if n is prime number
    :param n:
    :return: True if n is prime number
    """
    is_prime = True
    if n <= 1:
        is_prime = False
    else:
        for div in range(2, n):
            if n % div == 0:
                is_prime = False
                break
    return is_prime


def display_primes(limit: int):
    for i in range(2, limit):
        if is_prime(i):
            print(i)






if __name__ == '__main__':  # main + [tab]
    # # print(power(2, 8))
    # print(facto(5))
    # print(is_prime(13))
    display_primes(1000)
    assert power(2, 8) == 256
    assert facto(5) == 120
    assert is_prime(13)
