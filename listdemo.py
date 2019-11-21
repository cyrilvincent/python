l1 = [1,2,3]
l2 = list(l1)
l2.append(4)
print(l2)
print(l1)

def stats(l):
    min = l[0]
    max = l[0]
    sum = 0
    for i in l:
        sum +=i
        if i < min:
            min = i
        elif i > max:
            max = i
    return min, max, sum / len(l)

min, max, avg = stats(range(10))
print(min, max, avg)
