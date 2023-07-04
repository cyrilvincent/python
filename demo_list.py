l1 = [1,2,3,4]
l2 = range(1,5)

print(len(l1))
for i in l1:
    print(i)
print(3 in l1)
print(5 in l1)
print(l1[2])
print(l1[1:3])
print(l1[1:-1])

l1.append(5)
print(l1)
l1.insert(2,99)
print(l1)
print(l1.index(99))
l1.append(99)
print(l1)
print(l1.count(99))
l1.remove(99)
print(l1)
l1[2] = 98
print(l1)

l1.append(99)
print(l1)

for i in range(l1.count(99)):
    l1.remove(99)

print(l1)

sum = 0
for val in l1:
    sum += val
print(sum)

