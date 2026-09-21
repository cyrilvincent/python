# Porter factorielle, fibo et is_prime en fonction
# Bonus : typer les fonctions def factorielle(nb : int) -> int



def factorielle(nb: int) -> int:
    """
    Factorielle
    :param nb: nb
    :return: nb!
    """
    facto = 1
    for i in range(2, nb + 1):
        facto *= i
    return facto

def fibo(nb: int) -> int:
    f0 = 0
    f1 = 1
    fibo = 0
    for i in range(2, nb + 1):
        fibo = f0 + f1
        f0 = f1
        f1 = fibo
    return fibo

def is_prime(nb: int) -> bool:
    if nb < 2:
        return False
    for div in range(2, nb):
        if nb % div == 0:
            return False
    return True

print(factorielle(5))
print(fibo(10))
print(is_prime(7))