# Refaire la fonction range(x) qui créé une liste de 0 à x-1
# sum([1,2,3,4]) => 10
# max([1,2,3,4]) => 4
# add([1,2],[3,4]) => [4,6]
# filter_even([1,2,3,4]) => [2,4]
# Bonus : filter_prime([1,2,3,4]) => [2,3]
import tp_function

def range(nb: int) -> list[int]:
    l = []
    i = 0
    while i < nb:
        l.append(i)
        i += 1
    return l

def sum(l: list[float]) -> float:
    total = 0
    for value in l:
        total += value
    return total

def max(l :list[float]) -> float:
    result = l[0]
    for value in l[1:]:
        if value > result:
            result = value
    return result

def add(l1: list[float], l2: list[float]) -> list[float]:
    result = []
    for i in range(len(l1)):
        sum = l1[i] + l2[i]
        result.append(sum)
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
        if tp_function.is_prime(value):
            result.append(value)
    return result

if __name__ == '__main__':
    print(range(4))
    assert range(2) == [0,1]
    assert 10 == sum([1,2,3,4])
    assert 4 == max([1,2,3,4])
    assert [4,6] == add([1,2],[3,4])
    assert [2,4] == filter_even([1,2,3,4])
    assert [2,3] == filter_prime([1, 2, 3, 4])

