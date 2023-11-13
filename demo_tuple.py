from typing import List, Tuple
import scipy.stats


def min_max_avg(l: List[float]) -> Tuple[float, float, float]:
    min = max = sum = l[0]
    for i in l[1:]:
        sum += i
        if i < min:
            min = i
        if i > max:
            max = i
    return min, max, sum / len(l)

min, max, avg = min_max_avg([1,2,3,4])
print(min, max, avg)

