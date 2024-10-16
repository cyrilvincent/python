# a = (1, 2)
# print(a[0], a[1])
#
# def toto() -> tuple[float, int]:
#     return 1.0, 2
#
# a, b = toto()
# print(a, b)
#
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def min_max_avg(l: list[int]) -> tuple[int, int, float]:
    total = 0
    min = l[0]
    max = l[0]
    for value in l:
        total += value
        if value < min:
            min = value
        if value > max:
            max = value
    return min, max, total / len(l)

if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    min, max, avg = min_max_avg(l)
    print(min, max, avg)