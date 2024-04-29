l1 = [1,2,3]
l2 = l1
l1.append(4)
print(l1, l2)
print(l1 == l2, l1 is l2)

l1 = [1,2,3]
l2 = list(l1)
print(l1 == l2, l1 is l2)
l1.append(4)
print(l1, l2)
print(l1 == l2, l1 is l2)

print([1,2] is [1,2])

