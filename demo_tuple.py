# min_max_avg
# min_max_avg_dict -> dict[str, float]

def min_max_avg(l: list[int]) -> tuple[int, int, float]:
    """

    :param l:
    :return:
    """
    return 0, 10, 5


if __name__ == '__main__':
    min, max, avg = min_max_avg([])
    print(min, max, avg)

    l1 = [1,2,3]
    l2 = [4,5,6]
    print([x * y for x,y in zip(l1, l2)])