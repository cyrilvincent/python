# type simple by_value
a = 1
b = 2
b = a
b += 1
print(a, b)

# Reference type or Class
a = [1,2]
b = [1]
b = a
b.append(3)
print(a, b)

# Clone
a = [1,2]
b = [1]
b = list(a)
b.append(3)
print(a, b)

a = [1,2]
b = [1,2]
print(a == b, a is b)
a = b
print(a == b, a is b)

