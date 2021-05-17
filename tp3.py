# Saisir un chiffre: nb
# Afficher tous les nombres de 0 à nb-1
# Afficher tous les nombres de nb à 0 inclus
# Afficher si nb est pair ou impair
# Afficher si nb est un nombre premier ou non
# Un nombre divisible uniquement par 1 et lui même
# Tout nombre est premiers sauf si <= 1 et s'il possède un diviseur entre 2 et nb - 1
nb = int(input("Saisir un nb: "))
# for i in range(nb):
#     print(i)
# for i in range(nb, -1, -1):
#     print(i)
# print("Pair" if nb % 2 == 0 else "Impair")

is_prime = True
if nb <= 1:
    is_prime = False
else:
    for div in range(2, int(nb ** 0.5) + 1): # math.sqrt
        if nb % div == 0:
            is_prime = False
            break

print(f"{nb} est premier: {is_prime}")

