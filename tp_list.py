# Créer la liste l1=[1,2,38,99,7,99,25,57]
# Afficher la taille de la liste avec len
# Ajouter -1 entre 38 et 99
# Ajouter 200 en fin de liste
# Re afficher la taille de la liste
# Créer la fonction multiply qui * les éléments de la liste
# Créer la fonction max et min qui retourne le max et min de la liste
# Exemple max(l1) -> 200
# Bonus
# Créer une fonction remove_all(x) qui efface tous les x de la liste
# remove_all(l1, 99) -> retourne la liste sans les 99

def multiply(l):
    result = 1
    for value in l:
        result *= value
    return result

def max(l):
    max = l[0]
    for value in l:
        if value > max:
            max = value
    return max

def min(l):
    l.sort()
    return l[0]

def remove_all(l, value):
    nb = l.count(value)
    for _ in range(nb):
        l.remove(value)
    return l


l1=[1,2,38,99,7,99,25,57]
print(len(l1))
l1.insert(3, -1)
print(l1)
l1.append(200)
print(len(l1))
result = multiply(l1)
print(result)
print(max(l1))
print(min(l1))
print(remove_all(l1, 99))


