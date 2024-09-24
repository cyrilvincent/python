# Créer une liste avec 10 entiers "en dur" non consécutifs
# Afficher la longueur de la liste
# Créer la fonction sum(l: list[int]) -> int
# Créer la fonction average(l: list[int]) -> float
# Créer la fonction max(l: list[int]) -> int
# Créer la fonction filter_even(l: list[int]) -> list[int] : filter_even([1,2,3,4]) -> [2,4]
# Bonus : Créer la fonction filter_prime([1,2,3,4,5,6,7,8]) -> [2,3,5,7]
import tp3

def sum(l: list[int]) -> int:
    total = 0
    for value in l:
        total += value
    return total

def sum2(l: list[int]) -> int:
    total = 0
    for i in range(len(l)):
        total += l[i]
    return total

def average(l: list[int]) -> float:
    return sum(l) / len(l)

def max(l: list[int]) -> int:
    max = l[0]
    for value in l[1:]:
        if value > max:
            max = value
    return max

def max2(l: list[int]) -> int:
    l.sort()
    return l[-1]

def filter_even(l: list[int]) -> list[int]:
    res = []
    for value in l:
        if value % 2 == 0:
            res.append(value)
    return res

def filter_prime(l: list[int]) -> list[int]:
    res = []
    for value in l:
        if tp3.is_prime(value):
            res.append(value)
    return res

if __name__ == '__main__':
    l = [1,2,5,9,99,-1,0,8,14,50]
    print(sum(l))
    res = average(l)
    print(max(l))
    print(filter_even(l))
    print(filter_prime(l))

