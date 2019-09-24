def toto():
    return 1, 2

a, b = toto()
print(a)
print(b)

def minMaxAvg(l):
    min = l[0]
    max = l[0]
    sum = 0
    for i in l:
        if i < min:
            min = i
        elif i > max:
            max = i
        sum += i
    return min, max, sum / len(l)

t = minMaxAvg(range(100))
print(t)
# print(min)
# print(max)
# print(avg)