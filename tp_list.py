# Créer une liste de 10 valeurs "en dur" : l = [1, 99, 50, -1, 23, 45, 7, 11, 9, 10]
# Faire la fonction sum(l: list[float]) -> float
# Faire la fonction average
# Faire min et max
# + difficile : filter_even(l: list[int]) -> list[int] par exemple filter_even([1,2,3,4]) -> [2,4]
# Bonus : filter_prime([1,2,3,4,5]) -> [2,3,5]
import demo_function


def sum(l: list[float]) -> float:
    total=0
    for i in l:
        total+=i
    return total

def average(l: list[float]) -> float:
    return sum(l) / len(l)

def min(l: list[float]) -> float:
    min = l[0]
    for i in l:
        if i < min:
            min = i
    return min

def max(l: list[float]) -> float:
    l = list(l)
    l.sort()
    return l[-1]

def filter_even(l: list[float]) -> list[float]:
    result = []
    for i in l:
        if i % 2 == 0:
            result.append(i)
    return result

def filter_prime(l: list[int]) -> list[int]:
    result = []
    for i in l:
        if demo_function.is_prime(i):
            result.append(i)
    return result

if __name__ == '__main__':
    l = [1, 99, 50, -1, 23, 45, 7, 11, 9, 10]
    print(sum(l))
    print(average(l))
    print(min(l))
    print(max(l))
    print(filter_even(l))
    print(filter_prime(l))
