# Créer en dur une liste de 10 entiers
# Créer la fonction sum(l)
# Créer la fonction remove_all(l, value) remove_all([1,2,2,3], 2) => [1,3]
# Créer la fonction min, max
# Créer la fonction average

def sum(l):
    total = 0
    for value in l:
        total += value
    return total

def remove_all(l, value):
    for i in range(l.count(value)):
        l.remove(value)
    return l

def min(l):
    res = l[0]
    for value in l:
        if value < res:
            res = value
    return res

def min2(l1):
    l1.sort()
    return l1[0]

def max(l1):
    l1.sort()
    return l1[-1]

def avg(l):
    return sum(l) / len(l)

l1 = [0,1,2,99,4,99,6,-2,45,10]
res = sum(l1)
print(res)
res = remove_all(l1, 99)
print(res)
res = min(l1)
print(res)
res = min2(l1)
print(res)
res = max(l1)
print(res)
res = avg(l1)
print(res)

