from typing import Callable


def is_even(x: int) -> bool: # 8 % 2 == 0, 9 % 2 == 1
    """
    check if x is even
    :param x:
    :return:
    """
    return x % 2 == 0


def is_prime(x: int) -> bool : # Un nombre est premier si >2 et qu'il ne possède pas de diviseur entre 2 et n-1
    if x < 2:
        return False
    for div in range(2, int(x ** 0.5) + 1):
        if x % div == 0:
            return False
    return True

def max(l: list[float]) -> float:
    max = l[0]
    for v in l[1:]:
        if v > max:
            max = v
    return max

def evens(l: list[int]) -> list[int]: # [1,2,3,4] => [2,4]
    res = []
    for v in l:
        if v % 2 == 0:
            res.append(v)
    return res

# def filter(fn:Callable[[float], bool], l: list[float]) -> list[float]:
#     res = []
#     for v in l:
#         if fn(v):
#             res.append(v)
#     return res




if __name__ == '__main__':
    print(is_prime(7))
    print(is_prime(9))
    print(is_prime(4391))
    res = filter(is_prime, range(10000000000000000000000000000000000000000000000000000000000000000000000000000))
    res = filter(lambda x: x % 2 == 0, res)
    res = map(lambda x: x ** 2, res)
    for i in res:
        print(i)
