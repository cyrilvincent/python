# Saisir un nombre entier et le convertir en int() => nb
# Un nombre premier est un nombre qui a exactement 2 diviseurs : 1 et lui même
# Tout nombre > 1 est premier sauf s'il possède un diviseur

nb = 4391
if nb > 1:
    for div in range(2, nb):
        if nb % div == 0:
            print("Non premier")
            break
    print("Premier")
else:
    print("Non premier")

    # Créer la fonction is_prime(nb) -> bool