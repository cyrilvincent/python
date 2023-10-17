# Créer une liste de 10 entiers "en dur" l1 = [1,5,99,.....]
# Créer la fonction max(l1) -> le max
# Créer la fonction sum(l1) -> somme
# Créer la fonction average(l1) -> moyenne
# Créer la fonction remove_all(l1, value) -> remover toutes les valeurs value
# Bonus : filter_even(l1) -> retourne la liste avec le nb pairs filter_even([1,2,3,4]) => [2,4]
# Super bonus : filter_prime(l1)
import tp_function

def max(l):
    max=l[0]
    for val in l:
        if val > max:
            max = val
    return max

def max2(l):
    l.sort()
    return l[-1]

def sum(l):
    total = 0
    for val in l:
        total += val
    return total

def average(l):
    return sum(l) / len(l)

def remove_all(l, val):
    for _ in range(l.count(val)):
        l.remove(val)
    return l

def filter_even(l):
    res = []
    for val in l:
        if tp_function.is_even(val):
            res.append(val)
    return res

def filter_prime(l):
    res = []
    for val in l:
        if tp_function.is_prime(val):
            res.append(val)
    return res

def filter(fn, l):
    res = []
    for val in l:
        if fn(val):
            res.append(val)
    return res

l1 = [1, 2, 4, 99, 13, -2, 99, 48, 22, 10]
print(max2(l1))
print(sum(l1))
print(average(l1))
print(remove_all(l1, 99))
print(filter_even(l1))
print(filter_prime(l1))
print(filter(tp_function.is_prime, l1))

