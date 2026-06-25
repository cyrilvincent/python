# By Value
a = 1
b = a
a += 1
print(a, b)

# By reference
a = [1, 2]
b = a
a.append(3)
print(a, b)

# Clone
a = [1, 2]
b = list(a)  # a.copy()
a.append(3)
print(a, b)

a = [1,2]
b = [1,2]
print(a == b, a is b)
b = a
print(a == b, a is b)
a = None
print(a is None)