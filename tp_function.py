# Ecrice la fonction multiply(x, y) qui multiplie x et y + pydoc
# def factorielle(n: int) -> int 5! = 1*2*3*4*5 = 120
# def is_prime(n: int) -> bool Tout nb > 1 est premier sauf s'il possède un diviseur entre 2 et nb-1
# Bonus : fibonacci f(n) = f(n-1) f(n-2) avec f0 = 0 et f1=1

def multiply(x: float, y: float) -> float:
    """
    Multiply 2 numbers
    :param x: x
    :param y: y
    :return: x * y
    """
    return x * y

def factorielle(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorielle_rec(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorielle_rec(n - 1)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for div in range(2, n):
        if n % div == 0:
            return False
    return True


def fibo(n: int) -> int:
    f0 = 0
    f1 = 1
    fn = 0
    for i in range(n - 1):
        fn = f0 + f1
        f0 = f1
        f1 = fn
    return fn

def fibo_rec(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo_rec(n - 1) + fibo_rec(n - 2)


print(factorielle(5))
print(factorielle_rec(5))
print(is_prime(1223))
print(fibo(10))
print(fibo_rec(10))
