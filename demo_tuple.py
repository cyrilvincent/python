def min_max_avg(l: list[float]) -> tuple[float, float, float]:
    total = 0
    min = l[0]
    max = l[0]
    for value in l:
        total += value
        if value < min:
            min = value
        elif value > max:
            max = value
    return min, max, total / len(l)

min, max, avg = min_max_avg([1,2,3,4])
print(min, max, avg)