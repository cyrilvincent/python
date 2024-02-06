from typing import Tuple

def min_max_mean(l) -> Tuple[float, float, float]:
    sum = 0
    min = l[0]
    max = l[0]
    for value in l:
        sum += value
        if value < min:
            min = value
        if value > max:
            max = value
    return min, max, sum / len(l)

if __name__ == '__main__':
    l = [1,2,5,99,-1,5,-10,7,99,50]
    min, max, mean = min_max_mean(l)
    print(min, max, mean)