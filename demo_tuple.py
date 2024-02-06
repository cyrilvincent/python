from typing import Tuple


def min_max_mean(l) -> Tuple[float, float, float]:
    return 0,100,50

if __name__ == '__main__':
    l = [1,2,5,99,-1,5,-10,7,99,50]
    min, max, mean = min_max_mean(l)
    print(min, max, mean)