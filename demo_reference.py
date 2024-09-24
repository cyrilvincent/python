a = 1
b = a
a += 1
print(a, b)

a = [1,2]
b = a
a.append(3)
print(a, b)

a = [1,2]
b = list(a)
a.append(3)
print(a, b)