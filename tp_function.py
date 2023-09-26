# Créer la fonction factorielle
# Créer la fonction is_prime
# Tester

def factorielle(n: int) -> int:
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def is_prime(n: int) -> bool:
    """
    Retourne vrai si n est premier
    :param n: le nombre entier à tester
    :return: vrai si n est premier faux sinon
    """
    is_prime = True
    if n < 2:
        is_prime = False
    else:
        for div in range(2, n):
            if n % div == 0:
                is_prime = False
                break
    return is_prime

def add(* params):
    res = 0
    for value in params:
        res += value
    return res

if __name__ == '__main__':
    n = 5
    res = factorielle(n)
    print(res)
    res = is_prime(7)
    print(res)

    res = add()
    print(res)

    res = add(1)
    print(res)

    res = add(1,2,3)
    print(res)
