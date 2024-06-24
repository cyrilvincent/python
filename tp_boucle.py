# Faire une boucle avec while et for de 0 à 99 inclus
# Faire une boucle avec while et for de 99 à 0 inclus avec un pas de 3
# Afficher les nombres pairs inférieurs à 100
# Soit nb un nombre, afficher tous les diviseurs de nb (nb % div == 0 => div est un diviseur de nb)
# Bonus : dire si nb est premier

i = 0
while i < 100:
    print(i)
    i += 1

for i in range(100):
    print(i)

i=99
while i>= 0:
    print(i)
    i -= 3

for i in range(99, -1, -3):
    print(i)

for i in range(0,101,2):
    print(i)
    

nb = 4393
div_count = 0
for div in range(2, nb // 2 + 1):
    if nb % div == 0:
        print(f"{div} est un divisieur de {nb}")
        div_count += 1
if div_count == 0:
    print(f"{nb} est premier")
else:
    print(f"{nb} possède {div_count} diviseur(s)")


