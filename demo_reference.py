l1 = [1,2,3]
l2 = l1
l2.append(4)
print(l1)
print(l2)

l1 = [1,2,3]
l2 = list(l1)
l2.append(4)
print(l1)
print(l2)

l1 = [1,2,3]
l2 = [1,2,3]
print(l1 == l2)
print(l1 is l2)
l1 = l2
print(l1 == l2)
print(l1 is l2)
l1 = list(l2)
print(l1 == l2)
print(l1 is l2)
