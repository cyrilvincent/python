# Simple type <=> by value
a = 1
b = a
a += 1
print(a, b, a==b, a is b)

# Complex type <=> by ref
a = [1,2]
b = a
a.append(3)
print(a, b, a==b, a is b)

# Complex type <=> by clone
a = [1,2]
b = list(a)
a.append(3)
print(a, b, a==b, a is b)

a = [1,2]
b = [1,2]
print(a, b, a==b, a is b)