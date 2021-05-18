import math
import tp4

# Dans main créer la liste l1 avec 10 entiers en dur l1 = [1,9,8,3,3,7,....
# Filtrer les nombre pairs
# Ajouter 1 à la liste
# Filtrer les nombre pairs + Ajouter 1 à la liste
# Filtrer les nombres premiers et applique une racine carrée
# Appliquer un sin puis filtrer les sin > 0
# Bonus : Tester en enlevant la fonction list()
# Bonus essayer d'écrire un map + filter sur une seule ligne

l1 = [1,9,3,4,3,10,99,8,2,0]
res = list(filter(lambda x : x % 2 == 0, l1))
res = list(map(lambda x: x + 1, res))
print(res)
res = list(filter(lambda x : tp4.is_prime(x), l1))
res = list(map(lambda x: math.sqrt(x), res))
print(res)
res = list(map(lambda x: math.sin(x / 10), l1))
res = list(filter(lambda x : x > 0, res))
print(res)
print(list(map(lambda x: math.sqrt(x), filter(lambda x : tp4.is_prime(x), l1))))
