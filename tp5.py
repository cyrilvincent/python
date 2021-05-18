import math
import tp4
# from tp4 import is_even, is_prime, pi
# from math import pi

# Importer math et tester les fonctions de math
# Saisir un nb et dire s'il est premier ou non en réutilisant tp4
# Tester la différence entre import et from import en testant une collision de nom c'est à dire avoir une fonction is_prime dans tp5
# Tester tp4 dans un if __name__== ...
# Rendre le code robuste resaisir la données tant que vous être en erreur

stop = False
while not stop:
    try:
        nb = int(input("Saisir un nb: "))
        result = tp4.is_prime(nb)
        print(result)
        stop = True
    except ValueError as error:
        print(f"Erreur {error}")

