p1: tuple[float, float, float] = (3,2,-1)
print(p1)

def min_max_avg(l: list[int]) -> tuple[int, int, float]:
    sum = 0
    min = l[0]
    max = l[0]
    for v in l:
        sum += v
        if v < min:
            min = v
        elif v > max:
            max = v
    return min, max, sum / len(l)

l = [1,2,3,99,4,5,98,6,7,8,9]
min, max, avg = min_max_avg(l)
print(min, max, avg)
