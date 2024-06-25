def min_max_avg(l: list[int]) -> tuple[int, int, float]:
    sum = 0
    count = 0
    min = l[0]
    max = l[0]
    for value in l:
        count += 1
        sum += value
        if value < min:
            min = value
        if value > max:
            max = value
    return min, max, sum / count

min, max, avg = min_max_avg(list(range(100)))
print(min, max, avg)
