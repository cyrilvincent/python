# sum
# tester dans le if __name__=='__main__'
# max
# filter_even(l: list[int]) -> list[int] : [1,2,3,4] => [2,4]
# filter_prime(l: list[int]) -> list[int] : [1,2,3,4,5,6,7] => [2,3,5,7]

import tp_function


def sum(l: list[int]) -> int:
    """

    :param l:
    :return:
    """
    total = 0
    for val in l:
        total += val
    return total

def max(l: list[int]) -> int:
    result = l[0]
    for val in l[1:]:
        if val > result:
            result = val
    return result

def max2(l: list[int]) -> int:
    l2 = list(l)
    l2.sort()
    return l2[-1]


def filter_even(l: list[int]) -> list[int]:
    result = []
    for val in l:
        if val % 2 == 0:
            result.append(val)
    return result


def filter_prime(l: list[int]) -> list[int]:
    result = []
    for val in l:
        if tp_function.is_prime(val):
            result.append(val)
    return result

def input_list() -> list[int]:
    result = []
    while True:
        try:
            value = input("Saisir un entier: ")
            if value.strip() == "":
                break
            result.append(int(value))
        except ValueError as error:
            print("Merci de saisir un entier")
    return result

def square(l: list[float]) -> list[float]:
    result = []
    for val in l:
        result.append(val ** 2)
    return result


def stats(l: list[int]) -> tuple[float, int, int]:
    """

    :param l: 
    :return: min, max, avg 
    """
    sum = 0
    min = l[0]
    max = l[0]
    for val in l:
        sum += val
        if val > max:
            max = val
        elif val < min:
            min = val
    return sum / len(l), min, max

if __name__ == '__main__':
    l = [5, 99, 8, -2, 55, 52, 2006, 0, 18, 47]
    print(sum(l))
    print(max(l))
    print(filter_even(l))
    print(filter_prime(l))
    print(square(l))
    avg, min, max = stats(l)
    print(avg, min, max)
    res = input_list()
    print(res)