# Créer les fonctions facto, fibo, is_prime
# Typer : signature
# Tester

def factorielle(n: int) -> int:
    """
    Factorielle
    :param n:
    :return:
    """
    facto = 1
    for i in range(2, n + 1):
        facto *= i
    return facto

def fibonacci(n: int) -> int:
    fibo = 1
    fibo2 = 0
    for i in range(1, n):
        temp = fibo
        fibo = fibo + fibo2
        fibo2 = temp
    return fibo

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    is_prime = True
    for div in range(2, n):
        if n % div == 0:
            is_prime = False
            break
    return is_prime

if __name__ == '__main__':
    print(factorielle(5))
    print(fibonacci(10))
    print(is_prime(7))
    print(is_prime(8))
    assert factorielle(5) == 120