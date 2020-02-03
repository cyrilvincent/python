l = range(10)

def minMaxAvg(l):
    min = l[0]
    max = l[0]
    sum = 0
    for i in l:
        if i < min:
            min = i
        if i > max:
            max = i
        sum += i
    return min, max, sum / len(l)

res = minMaxAvg(l)
print(res)


