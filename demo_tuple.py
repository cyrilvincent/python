# min_max_avg
# min_max_avg_dict -> dict[str, float]

def min_max_avg(l: list[int]) -> tuple[int, int, float]:
    """

    :param l:
    :return:
    """
    min = l[0]
    max = l[0]
    sum = l[0]
    count = 1
    for v in l[1:]:
        sum += v
        if v < min:
            min = v
        elif v > max:
            max = v
        count += 1
    return min, max, sum / count

def min_max_avg_dict(l: list[int]) -> dict[str, float]:
    min, max, avg = min_max_avg(l)
    return {"min": min, "max": max, "avg": avg}


if __name__ == '__main__':
    min, max, avg = min_max_avg([])
    print(min, max, avg)

    l1 = [1,2,3]
    l2 = [4,5,6]
    print([x * y for x,y in zip(l1, l2)])