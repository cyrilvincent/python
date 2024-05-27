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


def is_prime(nb:int) -> bool:
    """
    Check if nb is prime number
    :param nb: nb to check
    :return: True if nb is prime
    """
    if nb > 1:
        for div in range(2, nb):
            if nb % div == 0:
                return False
        return True
    else:
        return False


res = is_prime(7)
print(res)

# Fonctions simples sur 1 ligne
# f(x) = x + 1
f = lambda x: x + 1
print(f(1))