from typing import List, Tuple
import scipy.stats


def min_max_avg(l: List[float]) -> Tuple[float, float]:
    min = 0.
    max = 99.
    return min, max

min, max = min_max_avg([1,2,3,4])
print(min, max)

