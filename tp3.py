# Faire une boucle de 0 à 100
# Faire un compte à rebourd de 10 à 0 puis afficher BOOM
# Saisir un chiffre et afficher tous les multiples de 3 inférieurs
#   Je saisis 10 => 0 3 6 9
# Saisir un chiffre et dire s'il est premier :
#   N est premier sauf s'il possède un diviseur entre 2 et N-1

nb = int(input("Saisir nb: "))
# for i in range(0,nb):
#     if i % 3 == 0:
#         print(i)

is_prime = True
if nb >= 2:
    for div in range(2,nb):
        if nb % div == 0:
            is_prime = False
            break

    print(is_prime)
else:
    print(False)

