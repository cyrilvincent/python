def min_max_avg(l: list[int]) -> tuple[int, int, float]:
    total = 0
    min = l[0]
    max = l[0]
    for v in l:
        total += v
        if v < min:
            min = v
        elif v > max:
            max = v
    return min, max, total / len(l)


min, max, avg = min_max_avg([1,2,3,4,5,6])
print(min, max, avg)