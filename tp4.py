# Créer une liste de 10 entiers en "dur"
# Créer la fonction sum(l) retourne la somme
# Créer la fonction mean(l) retourne la moyenne
# Créer la fonction remove_all(l, x) efface tous les x de l et retourne l
# BONUS : filter_even(l) => retourne une liste avec que les nombres pairs
# filter_even([1,2,3,4]) => [2,4]
# BONUS : filter_prime(l) => retourne une liste avec que les nombres premiers
# filter_prime([1,2,3,4,5,6]) => [2,3,5]
from typing import List
import tp3


def sum(l: List[float]) -> float:
    res = 0
    for value in l:
        res += value
    return res

def mean(l: List[float]) -> float:
    return sum(l) / len(l)

def remove_all(l: List[float], x: float) -> List[float]:
    for i in range(l.count(x)):
        l.remove(x)
    return l

def filter_even(l: List[float]) -> List[float]:
    res = []
    for value in l:
        if value % 2 == 0:
            res.append(value)
    return res

def filter_prime(l: List[float]) -> List[float]:
    res = []
    for value in l:
        if tp3.is_prime(value):
            res.append(value)
    return res




if __name__ == '__main__':
    l = [1,2,5,99,-1,5,-10,7,99,50]
    print(sum(l), mean(l))
    print(remove_all(l, 99))
    print(filter_even(l))
    print(filter_prime(l))
