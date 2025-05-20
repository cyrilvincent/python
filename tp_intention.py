# Créer une liste
# PAr intention : filtrer les nombres pairs
# Filtrer les nombres premiers
# Mettre au carré les éléments de la liste
# Filtrer les nombres premier et mettre au carré

import tp_function

l = [5, 99, 8, -2, 55, 52, 2006, 0, 18, 47]
res = [x ** 2 for x in l if tp_function.is_prime(x)]
print(res)