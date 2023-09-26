l1 = [1,2,3,4,99,0,99]
print(l1)
l2 = list(range(4,11,3))
print(l2)
print(l1[4])
for value in l1:
    print(value, end=" ")
print()
l1.append(999)
print(l1)
l1.remove(99) # By value
print(l1)
del l1[3] # By index
l1.append(99)
print(l1)

for i in range(l1.count(99)):
    l1.remove(99)

sum = 0
for value in l1:
    sum += value
print(sum)

print(0 in l1)
