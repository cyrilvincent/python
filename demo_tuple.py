from typing import List, Tuple, Iterator, Iterable


def return_multiple_values() -> Tuple[int, int, bool]:
    return 1, 0, True


def min_max_avg(l: List[float]) -> Tuple[float, float, float]:
    min = l[0]
    max = l[0]
    sum = 0
    for v in l:
        sum += v
        if v < min:
            min = v
        if v > max:
            max = v
    return min, max, sum / len(l)


if __name__ == '__main__':
    min, max, avg = min_max_avg(list(range(10))) # min = 0, max = 9, avg = 4.5
    print(min, max, avg)

