#Type valeur
a = 1
b = a
a += 1
print(a, b)

#Type reference
l1 = [1, 2]
l2 = l1
l1.append(3)
print(l1, l2)

#Type reference
l1 = [1, 2]
l2 = list(l1)
l1.append(3)
print(l1, l2)