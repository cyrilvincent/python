# Effacer les print de tp_function
# Créer une classe de test unitaire + 1 test par fonction
# Créer un module qui importe tp_function et saisir un nb et afficher sa factorielle, sa fibo, si le nb est premier ou non

import tp_function

while True:
    try:
        n = int(input("Saisir n: "))
        facto = tp_function.factorielle(n)
        print(f"{n}!={facto}")
        break
    except ValueError as ex:
        print(ex)
