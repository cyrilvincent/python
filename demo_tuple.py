t = (1,2)
print(t)

def min_max_avg(l: list[int]) -> tuple[int, int, float]:
    min = l[0]
    max = l[0]
    sum = 0
    len = 0
    for value in l:
        sum += value
        if value > max:
            max = value
        if value < min:
            min = value
        len += 1
    return min, max, sum / len

min, max, avg = min_max_avg([1,2,3,4])
print(min, max, avg)