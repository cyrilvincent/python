l1 = [10,8,77,5,-2,58,99]
print(l1)
for value in l1:
    print(value)
print(l1[2])
print(l1[-1])
print(l1[1:6])
print(l1[1:-1])
print(l1[2:-2])
index = l1.index(58)
print(index)
l1.append(999)
print(l1)
l1.remove(99)
print(l1)
l1[1]=888
print(l1)
