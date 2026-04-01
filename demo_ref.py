# By value
a = 1
b = a
a += 1
print(a, b)
print(a == b)

# By ref
a = [1, 2]
b = a
a.append(3)
print(a, b)
print(a == b, a is b)

# Clone
a = [1, 2]
b = list(a)
a.append(3)
print(a, b)
print(a == b, a is b)

# Même valeurs mais objets différents
a = [1, 2]
b = [1, 2]
print(a == b, a is b)