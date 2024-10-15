l = [1,2,3,99,4,5,6,99,7]
for i in range(l.count(99)):
    l.remove(99)
print(l)

total = 0
for value in l:
    if value % 2 == 0:
        print(value)
    total += value
print(total)