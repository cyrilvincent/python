# Créer la variable year = 2025
# Saisir vote année de naissance
# Afficher votre age en fin d'année

year = 2025
birth_string = input("Année de naissance: ")
birth_year = int(birth_string)
age = year - birth_year
print(f"Vous avez {age} ans")