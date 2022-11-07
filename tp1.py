# Saisir un entier positif
# Afficher si il est premier
# Tout nombre n > 1 est premier sauf s'il possède un diviseur entre 2 et n-1

x = int(input("Saisir un nombre: "))
if x < 2:
    print("Non premier")
    exit(0)
else:
    is_prime = True
    for div in range(2, x):
        if x % div == 0:
            is_prime = False
            break
    if is_prime == True:
        print("Est premier")
    else:
        print("Non premier")
