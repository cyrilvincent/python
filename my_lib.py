def is_prime(nb:int) -> bool:
    """
    Check if nb is prime number
    :param nb: nb to check
    :return: True if nb is prime
    """
    if nb > 1:
        for div in range(2, nb):
            if nb % div == 0:
                return False
        return True
    else:
        return False


def is_even(nb:int) -> bool:
    return nb % 2 == 0


if __name__ == '__main__':
    res = is_prime(7)
    print(res)
    res = is_even(8)
    print(res)

