# Créer la variable year = 2026
# Saisir votre année de naissance
# Afficher votre age en fin d'année

year = 2026
toto = 2
titi = 3
birth = input("Année de naissance: ")
birth = int(birth)
age = year - birth
print(f"Vous avez {age} ans")

condition = (year > 2026 or titi==3) and toto == 2
if condition:
    print("Trop grand")