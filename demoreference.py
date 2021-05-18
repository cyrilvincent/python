# Types valeurs : int, float, str, bool
a = 1
b = a
a = 2
print(a, b, a == b)

# Type référence : List
a = [1, 2]
b = a
a.append(3)
print(a, b, a == b)

# Clonage
def mylist(l):
    res = []
    for value in l:
        res.append(value)
    return res

a = [1, 2]
b = list(a)
a.append(3)
print(a, b, a == b)

a = [1,2,3]
b = list(a)
print(a == b, a is b)
a.append(4)
print(a == b, a is b)

a = [1,2,3]
b = a
a.append(4)
print(a == b, a is b)

print([1,2] == [1,2], [1,2] is [1,2])


