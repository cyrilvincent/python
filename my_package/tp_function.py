# Créer la fonction add(x,y)
# Créer la fonction max(x,y), min(x,y)
# Créer la fonction factorielle(n: int) -> int
# Créer la fonction fibo(n: int) -> int
# Créer la fonction is_prime(n: int) -> bool

def add(x: float, y: float) -> float:
    """
    Add 2 flaats
    :param x: 1st param
    :param y: 2nd param
    :return: x+y
    """
    return x + y


def max(x: float, y: float) -> float:
    if x > y:
        return x
    else:
        return y


def factorielle(n: int) -> int:
    if n < 0:
        raise ValueError("n < 0")
    fact = 1
    for i in range(n, 0, -1):
        fact *= i
    return fact


def factorielle2(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return n * factorielle2(n - 1)


def fibo(n: int) -> int:
    a = 0
    b = 1
    if n == 1:
        fibo = 1
    elif n == 0:
        fibo = 0
    else:
        for i in range(n - 1):
            fibo = a + b
            a = b
            b = fibo
    return fibo

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


def sum(*kargs: float) -> float:
    total = 0
    for value in kargs:
        total += value
    return total


if __name__ == '__main__':
    print(add(2,3))
    print(max(2,3))
    print(factorielle(5))
    print(is_prime(7))
    print(sum())
    print(sum(1))
    print(sum(1,2,3,4,5,6,7,8,9,0))
    factorielle(-1)

    toto = add
    print(toto(1,2))



