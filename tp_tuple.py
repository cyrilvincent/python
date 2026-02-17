def min_max_avg(l: list[float]) -> tuple[float, float, float]:
    min = l[0]
    max = l[0]
    sum = 0
    for v in l:
        sum += v
        if v < min:
            min = v
        elif v > max:
            max = v
    return min, max, sum/len(l)

if __name__ == '__main__':
    l = [1, 2, 5, 8, 99, 45, 61, -1, 9, 12]
    min, max, avg = min_max_avg(l)
    print(min, max, avg)