# Faire la fonction sum(l), max
# filter_even(l) -> List ex: filter_even([1,2,3,4]) => [2,4]
# filter_prime(l) -> List ex: filter_prime([1,2,3,4,5,6,7,8]) => [2,3,5,7] Reuse
# Bonus : filter
from typing import List
import tp_prime as prime

def sum(l: List[int]) -> int:
    sum = 0
    for i in l:
        sum += i
    return sum

def max(l : List[int]) -> int:
    max = l[0]
    for i in l[1:]:
        if i > max:
            max = i
    return max

def filter(fn, l: List[int]) -> List[int]:
    res = []
    for i in l:
        if fn(i):
            res.append(i)
    return res

def map(fn, l: List[int]) -> List[int]:
    res = []
    for i in l:
        res.append(fn(i))
    return res




if __name__ == '__main__':
    assert sum([1,2,3,4]) == 10
    assert max([1,2,3,4]) == 4
    assert filter(lambda x: x % 2 == 0, [1,2,3,4]) == [2,4]
    assert filter(prime.is_prime, [1, 2, 3, 4]) == [2, 3]
    assert map(lambda x: x + 1, [1,2,3,4]) == [2,3,4,5]

    # Even
    l = [1,2,3,4]
    res = [x for x in l if x % 2 == 0]
    print(res)

    # Map *2
    res = [x * 2 for x in l]
    print(res)

    # Filter + Map
    res = [x ** 2 for x in l if prime.is_prime(x)]
    print(res)

    volts = [10,20,30,40]
    amps = [1.1,1.3,1.6,1.9]
    res = [v * a for v, a in zip(volts, amps)]
    print(res)

    i = 0
    res = []
    while i < len(volts):
        v = volts[i]
        a = amps[i]
        res.append(v * a)
