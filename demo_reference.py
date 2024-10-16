# Value type
a = 1
b = a
a = a + 1
print(a, b)

# Reference type
a = [1, 2]
b = a
a.append(3)
print(a, b)
print(a == b, a is b)

# Clone
a = [1, 2]
b = list(a)
print(a == b, a is b)
a.append(3)
print(a, b)
print(a == b, a is b)

def modify_list(l):
    l.append(0)
    return l

a = [1,2]
modify_list(list(a))
print(a)
