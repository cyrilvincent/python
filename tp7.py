from typing import List, Callable
import demo_list_write
import tp4
import math


def is_positive_sin(x: float) -> bool:
    return math.sin(x) > 0


def filter_even(l: List[int]) -> List[int]:
    res = []
    for val in l:
        if val % 2 == 0:
            res.append(val)
    return res

def filter_prime(l: List[int]) -> List[int]:
    res = []
    for val in l:
        if tp4.is_prime(val):
            res.append(val)
    return res

def filter_generic(l: List[int], fn: Callable) -> List[int]:
    res = []
    for val in l:
        if fn(val):
            res.append(val)
    return res




# Faire pareil pour les nombres premiers : filter_prime
# Bonus = Créer filter_generic qui filtre n'importe en fonction d'une fonction passée en paramètre

if __name__ == '__main__':
    l = [1,2,3,4,5,6,7,8,9,10]
    res = filter_even(l)
    print(res) # => [2,4,6,8,10]
    l = demo_list_write.generate_random_list(10, 100)
    print(l)
    res = filter_even(l)
    print(res)
    res = filter_prime(l)
    print(res)
    res = filter_generic(l , tp4.is_prime)
    print(res)
    res = filter_generic(l, is_positive_sin)
    print(res)
    # Tester avec une list random