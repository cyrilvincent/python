# Créer la fonction power(x, y) qui effectue x ** y
# is_prime(nb: int) -> bool
# tester
# afficher tous les nb premier < 100

def power(x: float, y:float):
    return x ** y

def is_prime(nb : int) -> bool:
    """
    Compute prime number
    :param nb: nb to test
    :return: True if nb is prime
    """
    is_prime = True
    if nb < 2:
        is_prime = False
    else:
        for div in range(2, nb):
            if nb % div == 0:
                is_prime = False
                break
    return is_prime





def sqrt(x):
    return "toto"

if __name__ == '__main__':
    print(power(x=2,y=3))
    print(is_prime(7), is_prime(8))