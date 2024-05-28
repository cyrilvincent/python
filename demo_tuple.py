import datetime
import time


def min_max_avg(l) -> tuple[float, float, float]:
    min = l[0]
    max = l[0]
    sum = 0
    for value in l:
        if value < min:
            min = value
        if value > max:
            max = value
        sum += value
    return min, max, sum / len(l)


now = datetime.datetime.now()
min, max, avg = min_max_avg(range(1000000))
after = datetime.datetime.now()
print(after - now)

print(min, max, avg)

