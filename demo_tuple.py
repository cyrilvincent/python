def min_max_avg(l: list[int]) -> tuple[int, int, float]:
    min = 0
    max = 99
    sum = 500
    return min, max, sum/len(l)


min, max, avg, toto = min_max_avg([1,2,3,4,5,6])
print(min, max, avg)