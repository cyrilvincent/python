# sum
# min
# max
# mean
# filter_even(list: list[int]) -> list[int] filter_even([1,2,3,4]) -> [2,4]
# Astuce : créer une liste vide qu'on append au fur et à mesure
# Bonus : filter_prime([1,2,3,4,5,6,7]) -> [2,3,5,7]
# Bonus afficher tous les nb premiers < 1000
# import + function + main + test

import tp_function as tp

def sum(list: list[float]) -> float:
    total = 0
    for value in list:
        total += value
    return total

def min(list: list[float]) -> float:
    min = list[0]
    for value in list:
        if value < min:
            min = value
    return min

def max(list: list[float]) -> float:
    max = list[0]
    for value in list:
        if value > max:
            max = value
    return max

def mean(list: list[float]) -> float:
    return sum(list) / len(list)

def filter_even(list: list[int]) -> list[int]:
    result = []
    for value in list:
        if value % 2 == 0:
            result.append(value)
    return result

def filter_prime(list: list[int]) -> list[int]:
    result = []
    for value in list:
        if tp.is_prime(value):
            result.append(value)
    return result

if __name__ == '__main__':
    print(sum([1,2,3,4]))
    print(min([2,1,3]))
    print(max([1,2,4,3]))
    print(mean([1,2,3,4]))
    l = [1.1,2.,3.,4.]
    print(filter_even(l))
    print(filter_prime([1,2,3,4,5,6,7]))