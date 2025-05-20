# Créer une liste de 10 entiers non ordonnés
# Afficher les 10 valeurs
# Afficher le sous ensemble de l'index 4 à 7 inclus
# Sommer les éléments de la liste
# Trouver le max

l = [5,99,8,-2,55,52,2006,0,18,47]

for val in l:
    print(val)

sub = l[4:8]
print(sub)

sum = 0
for val in l:
    sum += val
print(sum)

max = l[0]
for val in l[1:]:
    if val > max:
        max = val
print(max)

l.sort()
max = l[-1]

def my_function(l: list[float]) -> list[float]:
    pass


