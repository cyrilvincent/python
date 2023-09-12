# Créer la fonction puissance(x,y) => x ** y
# Créer la fonction is_even(x) renvoie True si x est pai, False sinon
# Créer la fonction is_prime(x) idem pour les nombre premier
# A tester

def power(x, y):
    return x ** y

def is_even(x: int) -> bool:
    """
    Return True if x is even
    :param x: nb
    :return: True if even
    """
    if x % 2 == 0:
        return True
    else:
        return False

def is_prime(nb):
    if nb < 2:
        return False
    else:
        is_prime = True
        for div in range(2, int(nb ** 0.5) + 1):
            if nb % div == 0:
                is_prime = False
                break
        return is_prime

if __name__ == '__main__':
    print(power(2,3))
    print(is_even(8))
    print(is_prime(7))
    result = is_even(8)


