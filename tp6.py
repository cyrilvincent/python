# Dans main créer la liste l1 avec 10 entiers en dur l1 = [1,9,8,3,3,7,....
# Créer la fonction display qui affiche le contenu de la liste
# Créer la fonction remove_all(3) efface TOUT les 3 de la liste
# Créer la fonction sum(l) -> somme des éléments de la liste, 0 si la liste est vide
# Créer la fonction max(l) -> max, plante si la liste est vide
# Bonus, add(l1, l2) = l1 + l2 add([1,2], [3,4]) => [4,6]

def display(l):
    for value in l:
        print(value, end=' ')
    print()

def remove_all(l, value):
    count = l.count(value)
    for _ in range(count):
        l.remove(value)

def sum(l):
    total = 0
    for value in l:
        total += value
    return total

def max(l):
    res = l[0]
    for value in l:
        if value > res:
            res = value
    return res

def add(l1, l2):
    res = []
    if len(l1) == len(l2):
        index = 0
        for _ in l1:
            res.append(l1[index] + l2[index])
            index += 1
    return res

def add2(l1, l2):
    res = []
    if len(l1) == len(l2):
        for index, value in enumerate(l1):
            res.append(value + l2[index])
    return res


if __name__ == '__main__':
    l1 = [1,9,3,4,3,10,99,8,-2,0]
    l1[0] = -99
    display(l1)
    remove_all(l1, 3)
    print(l1)
    print(sum(l1))
    print(max(l1))
    print(add([1,2], [3,4]))
