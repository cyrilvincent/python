# Créer une liste de 10 entiers
# Filtrer les nombres premier avec filter
# Passer au carré tous les éléments de la liste avec un map
# Filtrer les nombre premier de la liste et les monter au carré filter + map
# Filtrer les nombres premier avec une liste en intention
# Passer au carré tous les éléments de la liste avec une liste en intention
# Filtrer les nombre premier de la liste et les monter au carré avec une liste en intention
import tp3

l = [1,2,5,9,99,-1,0,8,14,50]
res = filter(tp3.is_prime, l)
print(list(res))

res = map(lambda x: x ** 2, l)
print(list(res))

res = map(lambda x: x ** 2, filter(tp3.is_prime, l))
print(list(res))

res = [x ** 2 for x in l if tp3.is_prime(x)]
print(res)
