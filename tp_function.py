def is_prime(n: int) -> bool:
    """
    Compute prime number
    :param n: the number
    :return: true if n is prime
    """
    is_prime = True
    if n < 2:
        is_prime = False
    else:
        for div in range(2, int(n ** 0.5) + 1):
            if n % div == 0:
                is_prime = False
                break
    return is_prime


def is_even(n: int) -> bool:
    """
    Retourne vrai si pair
    :param n: nb à tester
    :return: True if even
    """
    return n % 2 == 0


if __name__ == '__main__':
    res = is_prime(7)
    print(res)
    print(is_even(8))
    print(is_even(7))

