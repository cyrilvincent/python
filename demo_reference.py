# Value type
a = 1
b = a
a += 1
print(a, b)

# Reference type
a = [1, 2]
b = a
a.append(3)
print(a, b)

# Reference type + clone
a = [1, 2]
b = list(a)
a.append(3)
print(a, b)

def hello(l):
    l.append(99)

a = [1,2]
hello(a)
print(a)

a = [1,2]
b = [1,2]
print(a == b, a is b)
a = b
print(a == b, a is b)
a = list(b)
print(a == b, a is b)