# Saisir un age
# Afficher une erreur si age n'est pas un int : int(age)
# Resaisir l'age tant que l'age n'est pas bon
import tp_function

while True:
    try:
        n = input("Saisir n pour calculer n!: ")
        n = int(n)
        result = tp_function.factorielle(n)
        print(f"{n}!={result}")
        break
    except ValueError as ex:
        print(f"Error {ex}")

