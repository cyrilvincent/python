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


if __name__ == '__main__':
    res = is_prime(7)
    print(res)

