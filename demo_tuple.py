p1: tuple[float, float, float] = (3,2,-1)
print(p1)

def min_max_avg(l: list[int]) -> tuple[int, int, float]:
    min = 0
    max = 99
    avg = 50
    return min, max, avg

l = [1,2,3,99,4,5,98,6,7,8,9]
min, max, avg = min_max_avg(l)
print(min, max, avg)
