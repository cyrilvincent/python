from typing import List, Tuple

t = (1,2,3)
print(t)

def myfunc(x):
    return 1,2,3

t = myfunc(0)
print(t[0])
print(t[1])
print(t[2])

a, b, c = myfunc(0)
# TP
# Créer la fonction min_max_avg(l) -> Tuple contenant le min, max et avg
def min_max_avg(l: List[float]) -> Tuple[float, float, float]:
    max = l[0]
    min = l[0]
    sum = 0
    for val in l:
        sum += val
        if val < min:
            min = val
        if val > max:
            max = val
    return min, max, sum / len(l)

min, max, avg = min_max_avg([1,2,3,4,5])
print(min, max, avg)

