a = 1
b = a # By value
a += 1
print(a, b)

a = [1, 2]
b = a # By reference
a.append(3)
print(a, b)

a = [1, 2]
b = list(a) # By cloned
a.append(3)
print(a, b)

print([1,2] == [1,2], [1,2] is [1,2])
a = [1, 2]
b = [1, 2]
print(a == b, a is b)
b = a
print(a == b, a is b)
a = [1, 2]
b = [1]
print(a == b, a is b)