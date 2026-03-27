# Refaire depuis tp_list les fonction square, filter_even, filter_prime
# Faire la fonction min_max_avg(l: list[float]) -> tuple[float, float, float]
# min, max, avg = min_max_avg([1,2,3,4])
# assert min == 1
# assert max = 4
# assert avg = 2.5

import tp_function as tp


def filter_prime(l: list[float]) -> list[float]:
    return [x for x in l if tp.is_prime(x)]

def min_max_avg(l: list[float]) -> tuple[float, float, float]:
    min = l[0]
    max = l[0]
    sum = 0
    for value in l:
        sum += value
        if value < min:
            min = value
        elif value > max:
            max = value
    return min, max, sum/len(l)


if __name__ == '__main__':
    assert filter_prime([2,3,4,5,6]) == [2,3,5]
    min, max, avg = min_max_avg([1,2,3,4])
    assert min == 1
    assert max == 4
    assert avg == 2.5