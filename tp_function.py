# Créer la fonction sum_cumul(n) => sum_cumul(10) = 55
# idem pour factorielle, fibonacci et is_prime (Typage + PyDoc """)
# Bonus Créer la fonction qui "affiche" tous les nombre premiers < 1000

def sum_cumul(n: int) -> int:
    """
    Somme de 0 à n
    :param n:
    :return:
    """
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum

def factorielle(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def finonacci(n: int) -> int:
    f0 = 0
    f1 = 1
    result = 0
    for i in range(2, n + 1):
        result = f0 + f1
        f0 = f1
        f1 = result
    return result

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def display_primes(limit: int):
    for i in range(2, limit):
        if is_prime(i):
            print(i)


print(sum_cumul(10))
print(factorielle(5))
print(finonacci(10))
print(is_prime(7919))
display_primes(1000)