# import math
# Afficher une tanh
# modifier tp_function pour que les tests soient dans un if __name__ == '__main__':
# importer tp_function
# tester les fonctions
# Créer un package my_package
# Déplacer tp_functions dans my_package
# Corriger le code

import math
import my_package.tp_function as tp

print(math.tanh(0))
print(tp.factorielle(5))

while True:
    try:
        i = int(input("saisir: "))
        if i < 0:
            raise ValueError("i < 0")
        break
    except ValueError as ex:
        print(f"Error {ex}")




