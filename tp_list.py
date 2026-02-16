# Créer une liste "en dur" avec 10 entiers non consécutifs
# Afficher la liste
# Faire la fonction sum(l: list[float]) -> float
# Idem pour average
# Faire la fonction max
# Faire la fonction qui retourne la liste des puissance de 2 : power2(n) par exemple power2(5) => [1,2,4,8,16,32]
# Bonus filter_prime(l: list[int])-> list[int] par exemple filter_prime([1,2,3,4,5,6,7,8,9,10]) => [2,3,5,7]

import tp3
import math

def sum(l: list[float]) -> float:
    result = 0
    for v in l:
        result += v
    return result

def max(l: list[float]) -> float:
    result = l[0]
    for v in l[1:]:
        if v > result:
            result = v
    return result

def power2(n: int) -> list[int]:
    l = []
    for i in range(n + 1):
        l.append(2 ** i)
    return l

def filter_prime(l: list[int]) -> list[int]:
    result = []
    for v in l:
        if tp3.is_prime(v):
            result.append(v)
    return result

def double(l: list[float]) -> list[float]:
    result = []
    for v in l:
        result.append(v * 2)
    return result


if __name__ == '__main__':
    l = [1, 2, 5, 8, 99, 45, 61, -1, 9, 12]
    print(sum(l))
    print(max(l))
    print(power2(8))
    print(filter_prime(l))
    print(double(l))

    res = [math.cos(x) ** 2 for x in l]
    print(res)
    filter = [x for x in l if x % 2 == 0]
    print(filter)
    filter = [x for x in l if tp3.is_prime(x)]
    print(filter)
    filter = [x ** 2 for x in l if tp3.is_prime(x)]
    print(filter)
