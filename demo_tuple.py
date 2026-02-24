def min_max_avg(l: list[float]) -> tuple[float, float, float]:
    sum = 0
    min = l[0]
    max = l[0]
    for v in l:
        sum += v
        if v > max:
            max = v
        elif v < min:
            min = v
    return min, max, sum / len(l)

if __name__ == '__main__':
    l = [1, 99, 50, -1, 23, 45, 7, 11, 9, 10]
    min, max, avg = min_max_avg(l)
    print(min, max, avg)
