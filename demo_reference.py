# Simple Type = By Value

a = 1
b = 2
a = b
a += 1
print(a, b, a == b)

# Complex Type = By Ref
a = [1,2]
b = [3,4]
a = b
a.append(5)
print(a, b, a == b, a is b)

# Clone
a = [1,2]
b = [3,4,]
a = list(b)
a.append(5)
print(a, b, a == b, a is b)

a = [1,2]
b = [1,2]
print(a == b, a is b)

