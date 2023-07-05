from typing import Tuple, List
import tp6


def my_function_tuple() -> Tuple[int ,int]:
    return 0, 10

x, y = my_function_tuple()
print(x, y)

def min_max_avg(l: List[float]) -> Tuple[float, float, float]:
    min = l[0]
    max = l[0]
    sum = 0
    for val in l:
        sum += val
        if val < min:
            min = val
        if val > max:
            max = val
    return min, max, sum / len(l)

# TP
# Créer la fonction min_max_avg(l: List[float]) -> Tuple[float, float, float]
