# Créer "en dur" l = [1,2,5,99,10,-1,0,99,88,41] une liste avec 10 entiers
# Afficher le premier et le dernier élément de la liste
# Effacer le premier 99
# Ajouter en fin de liste 999
# Faire la fonction sum(l) -> sum([1,2,3]) => 6
# Faire la fonction max(l) max([1,2,3]) => 3
# + difficile filter_even([1,2,3,4]) => [2,4] il faut créer une nouvelle liste vide
# Bonus filter_prime([1,2,3,4,5,6,7,8,9]) => [2,3,5,7]

def sum(l):
    total = 0
    for i in l:
        total += i
    return total



if __name__ == '__main__':
    l = [1, 2, 5, 99, 10, -1, 0, 99, 88, 41]
    print(l[0], l[-1])
    l.remove(99)
    l.append(999)
    print(l)
    print(sum(l))