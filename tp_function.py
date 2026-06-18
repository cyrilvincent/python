# Faire la fonction add(x, y)
# is_even(x: int) -> bool
# factorielle(n: int) -> int
# fibo(n: int) -> int
# is_prime(n: int) -> bool
# docstring

def is_even(x: int) -> bool:
    """
    Docstring for is_even
    
    :param x: Description
    :type x: int
    :return: Description
    :rtype: bool
    """
    return x % 2 == 0


def factorielle(n: int) -> int:
    facto = 1
    for i in range(2, n + 1):
        facto *= i
    return facto


def fibo(n: int) -> int:
    f0 = 0
    f1 = 1
    fibo = 0
    for _ in range(n - 1):
        fibo = f0 + f1
        f0 = f1
        f1 = fibo
    return fibo

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for div in range(2, n):
        if n % div == 0:
            return False
    return True

if __name__ == "__main__":
    assert factorielle(5) == 120
    assert fibo(10) == 55
    assert is_prime(7)
