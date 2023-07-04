# Faire la fonction is_prime(nb) -> bool
# Tester avec plein de chiffres différents

def is_prime(nb: int) -> bool:
    """
    Calcul si nb est premier
    :param nb: nombre à tester
    :return: True si premier False sinon
    """
    is_prime = True
    if nb >= 2:
        for div in range(2, nb):
            if nb % div == 0:
                is_prime = False
                break
        return is_prime
    else:
        return False

if __name__ == '__main__':
    result = is_prime(7)
    print(result)
    print(is_prime(9))

    for i in range(100):
        print(f"{i}: {is_prime(i)}")