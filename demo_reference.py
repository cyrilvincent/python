a = 1
b = a
a = a + 1
print(a, b, a==b, a is b)

a = [1]
b = a
a.append(2)
print(a, b, a==b, a is b)

a = [1]
b = list(a)
a.append(2)
print(a, b, a==b, a is b)

a = [1,2]
b = [1,2]
print(a == b, a is b)
b = a
print(a == b, a is b)