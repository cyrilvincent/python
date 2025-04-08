def f(x):
    return x + 1

def add(a, b):
    """
    Add 2 numbers
    :param a: first param
    :param b: second param
    :return: a + b
    """
    return a + b

# def my_complex_function(toto, titi, tata, x=1, y=2, z=3):
#     pass


# my_complex_function(toto=1, titi=2, x=5)

result = f(3)
print(result)

print(f(3))

result = add(3,2)
print(result)

add(3,2)


def mesure(value: float, unit: str) -> float:
    return 3.14


result = mesure(value=3.14, unit=1)


def factorielle(n: int) -> int:
    """
    Factorielle
    :param n: parameter
    :return: n!
    """
    facto = 1
    for i in range(2, n + 1):
        facto *= i
    return facto

res = factorielle(5)
print(res)

def parameter_tuple(*params):
    for p in params:
        print(p)

def add(*kargs):
    sum = 0
    for arg in kargs:
        sum += arg
    return sum

print(add(1,2))

def cos(x):
    return 0

