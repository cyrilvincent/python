# Faire la fonction multiply(a, b)
# Tester
# Faire la fonction factorielle(n: int) -> int
# Faire la fonction fibo(n: int) -> int
# Faire la fonction is_prime(n: int) -> bool

def multiply(a: float, b: float) -> float:
    """
    Multiply
    :param a:
    :param b:
    :return:a*b
    """
    return a * b

def factorielle(n: int) -> int:
    """
    Factorielle
    :param n:
    :return: n!
    """
    facto = 1
    for i in range(1, n + 1):
        facto *= i
    return facto

def fibo(n: int) -> int:
    """
    Fibonacci f(n) = f(n-1) + f(n-2)
    :param n:
    :return: f(n-1) + f(n-2)
    """
    f0 = 0
    f1 = 1
    fibo = 0
    for i in range(1, n):
        fibo = f0 + f1
        f0 = f1
        f1 = fibo
    return fibo

def is_prime(n: int) -> bool:
    for div in range(2, n):
        if n % div == 0:
            return False
    return True

def multiply(*kargs):
    result = 1
    for k in kargs:
        result *= k
    return result

def matplotlib(**kwargs):
    for key in kwargs:
        print(key, kwargs[key])



def f(x):
    return x +1

f = lambda x: x + 1


if __name__ == '__main__':


    print(multiply(2,3))
    print(factorielle(5))
    print(fibo(10))
    print(is_prime(7))
    print(multiply(2,3,4))
    matplotlib(toto="titi", tata="tutu")