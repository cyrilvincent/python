def min_max(l):
    return 0, 99

l1 = [0,1,2,7,5,99,6,-2,11,10]
min, max = min_max(l1)
print(min, max)

def min_max_avg(l):
    min = max = l[0]
    total = 0
    for value in l:
        total += value
        if value < min:
            min = value
        if value > max:
            max = value
    return min, max, total / len(l)

min, max, avg = min_max_avg(l1)
print(min, max, avg)
