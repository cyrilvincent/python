# Dans des fonctions + tests
# sum
# multiply
# min & max
# square [1,2,3] => [1,4,9]
# filter_even : filtre que les pairs [1,2,3,4] => [2,4]
# Bonus : filter_prime [1,2,3,4,5] => [2,3,5]
# Bonus : refaire la fonction sum par index
# Bonus : fibo(5) = fibo(n) = fibo(n-1) + fibo(n-2)
import tp_function as tp

def multiply(l: list[float]) -> float:
    total = 1
    for value in l:
        total *= value
    return total

def min(l: list[float]) -> float:
    min = l[0]
    for value in l:
        if value < min:
            min = value
    return min

def max(l: list[float]) -> float:
    max = l[0]
    for value in l:
        if value > max:
            max = value
    return max

def square(l: list[float]) -> list[float]:
    result = []
    for value in l:
        result.append(value ** 2)
    return result

def filter_even(l: list[int]) -> list[int]:
    result = []
    for value in l:
        if value % 2 == 0:
            result.append(value)
    return result

def filter_prime(l: list[int]) -> list[int]:
    result = []
    for value in l:
        if tp.is_prime(value):
            result.append(value)
    return result

def sum_by_index(l: list[float]) -> float:
    total = 0
    for i in range(len(l)):
        total += l[i]
    return total

def fibo(n: int) -> int:
    f0 = 0
    f1 = 1
    fn = f0 + f1
    for i in range(2, n+1):
        fn = f0 + f1
        f0 = f1
        f1 = fn
    return fn


if __name__ == '__main__':
    assert multiply([2,3,4]) == 24
    assert min([2,1,3]) == 1
    assert max([2, 1, 3]) == 3
    assert square([1,2,3]) == [1,4,9]
    assert filter_even([1,2,3,4]) == [2,4]
    assert filter_prime([2,3,4,5,6,7,8,9]) == [2,3,5,7]
    assert fibo(10) == 55