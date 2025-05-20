l = [5, 99, 8, -2, 55, 52, 2006, 0, 18, 47]

res = [x * 2 for x in l] # MAP renvoie une nouvelle liste avec les valeurs modifiée (même longueur)
print(res)

res = [x for x in l if x % 2 == 0]
print(res) # FILTER len sont différentes

res = [x * 2 for x in res] # Maladroit
print(res)

res = [x * 2 for x in l if x % 2 == 0]

