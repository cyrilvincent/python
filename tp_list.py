import tp_function

def sum(l: list[float]) -> float:
    total = 0
    for value in l:
        total += value
    return total

def mean(l: list[float]) -> float:
    return sum(l) / len(l)

def min(l: list[float]) -> float:
    mini = l[0]
    for value in l:
        if value < mini:
            mini = value
    return mini

def max(l: list[float]) -> float:
    l.sort()
    return l[-1]

def filter_even(l: list[float]) -> list[float]:
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

# def mean
# def min
# def max
# difficile : filter_even([1,2,3,4]) -> [2,4]
# +difficile : filter_prime([1,2,3,4,5]) -> [2,3,5]

if __name__ == '__main__':
    assert sum([1,2,3,4,5]) == 15
    assert sum([]) == 0
    assert mean([1,2,3,4,5]) == 3
    assert min([1,2,3,4]) == 1
    assert max([1,2,3,4]) == 4
    assert filter_even([1,2,3,4]) == [2,4]
    assert filter_prime([1, 2, 3, 4]) == [2, 3]
