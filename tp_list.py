

# Créer la fonction sum(l: list[float]) -> float
# idem max
# multiply [1,2,3,4] -> 1*2*3*4 = 24

# + difficile
# Créer la fonction filter_even(l: list[int]) -> list[int] exemple filter_event([1,2,3,4]) -> [2,4]
# tips : Dans la fonctioner penser à créer une liste vide
# bonus
# filter_prime(l: list[int]) -> list[int] exemple filter_prime([1,2,3,4,5,6,7,8]) -> [2,3,5,7]

import my_package.tp_function as tp


def sum(l: list[float]) -> float:
    total = 0
    for v in l:
        total += v
    return total

def max(l: list[float]) -> float:
    max = l[0]
    for v in l[1:]:
        if v > max:
            max = v
    return max

def multiply(l: list[float]) -> float:
    total = 1
    for v in l:
        total *= v
    return total

def filter_even(l: list[int]) -> list[int]:
    res = []
    for v in l:
        if v % 2 == 0:
            res.append(v)
    return res

def filter_prime(l: list[int]) -> list[int]:
    res = []
    for v in l:
        if tp.is_prime(v):
            res.append(v)
    return res


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(sum(l))
    print(max(l))
    print(multiply(l))
    print(filter_even(l))
    print(filter_prime(l))

