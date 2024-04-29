
def is_prime(nb: int) -> bool:
    """
    fgfgdrhd
    :param nb:
    :return:
    """
    if nb > 1:
        for div in range(2, nb):
            if nb % div == 0:
                return False
        return True
    return False


if __name__ == '__main__':
    print("Hello World!")

    s = input("Saisir x: ")
    x = int(s)


    print(is_prime(x))
