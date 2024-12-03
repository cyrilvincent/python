# Créer la fonction add(a,b)
# Créer la fonction is_even(n) => retourne True si n est pair False sinon
# Créer la fonction sums(n) = somme de 0 à n inclus 5=>1+2+3+4+5
# Créer la fonction factorielle(n) => n! pour n > 0
# Créer la fonction fibo(n) => fibo(10) => 55
# Créer la fonction is_prime(n) => retourne True si n est premier False sinon
# Tester

import math as m
m.cos(0)

# from math import cos
# cos(0)


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def sums(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

def factorielle(n):
    if n < 1 or type(n) != int:
        raise ValueError("N must be >= 1")
    factorielle = 1
    for i in range(2, n+1):
        factorielle *= i
    return factorielle

def fibo(n):
    a = 1
    b = 0
    for i in range(2, n + 1):
        fibo = a + b
        b = a
        a = fibo
    return fibo

def is_prime(n):
    """

    :param n:
    :return: boolean True if prime
    """
    if n < 2:
        return False
    else:
        for div in range(2, int(n ** 0.5) + 1):
            if n % div == 0:
                return False
        return True

def cos(n):
    return "toto"


if __name__ == '__main__':
    print(is_even(8), is_even(7))
    print(sums(5))
    print(factorielle(10))
    print(fibo(15))
    print(is_prime(7), is_prime(10), is_prime(1223))

