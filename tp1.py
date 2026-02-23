# Créer la variable year = 2026
# Saisir votre année de naissance
# Afficher votre age en fin d'année

year = 2026
birth = input("Année de naissance: ")
birth_int = int(birth)
age = year - birth_int
print(f"Vous avez {age} ans")