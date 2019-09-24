l1 = [1,2,3]
print(l1)
l2 = l1
l1.append(4)
print(l2)

print(l1 is l2)

l2 = list(l1)