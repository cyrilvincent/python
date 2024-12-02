# Créer la variable a = 1 et b = 2
# Permuter a et b
# Saisir un nombre
# Afficher le nombre de chiffre, 50 => 2
# * par 2 le nombre et l'afficher
# Afficher 0 si le nombre est pair et 1 sinon

a = 1
b = 2
c = a
a = b
b = c
print(a, b)
a, b = b, a

nb = input("Saisir un nb: ")
print(f"Ce nombre possède {len(nb)} chiffre(s)")
nb = int(nb)
print(f"Le nombre *2 = {nb * 2}")
print(nb % 2)

