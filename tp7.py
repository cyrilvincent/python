a = 1
b = a
b += 1
print(a, b)

l1 = [1,2,3]
l2 = l1
print(l1 == l2)
print(l1 is l2)
l1.append(4)
print(l1, l2)


l1 = [1,2,3]
l2 = list(l1)
print(l1 == l2)
print(l1 is l2)
l1.append(4)
print(l1, l2)

