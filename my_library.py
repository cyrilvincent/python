import math

def sum(l: list[float]) -> float:
    sum = 0
    for value in l:
        sum += value
    return sum

def mean(l: list[float]) -> float:
    return sum(l) / len(l)

def max(l: list[float]) -> float:
    max = l[0]
    for value in l[1:]:
        if value > max:
            max = value
    return max

def double(l: list[float]) -> list[float]:
    """
    [1,2,3,4] -> [2,4,6,8]
    :param l:
    :return:
    """
    result = []
    for value in l:
        result.append(value * 2)
    return result

# Bonus
def filter_even(l: list[float]) -> list[float]:
    """
    [1,2,3,4] => [2,4]
    :param l:
    :return:
    """
    result = []
    for value in l:
        if value % 2 == 0:
            result.append(value)
    return result

def min_max_mean(l: list[float]) -> tuple[float, float, float]:
    pass

if __name__ == '__main__':
    l = [1,2,3,4,5,6,7,8,9,10]
    print(sum(l))
    print(mean(l))
    print(max(l))
    print(double(l))
    print(filter_even(l))
    result = [math.cos(x) for x in l if x % 3 == 0]
    print(result)