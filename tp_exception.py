import datetime

# datetime.datetime.now().year
# Saisir votre année de naissance et calculer votre age en fin d'année
# Gérer les erreurs
# Resaisir tant qu'il y a une erreur
# Bonus gérer les années < 0 année > aujourd'hui

actual_year = datetime.datetime.now().year
while True:
    try:
        birth_year = int(input("Année de naissance: "))
        age = actual_year - birth_year
        if not(0 <= age < 120): # age < 0 or age > 120
            raise ValueError("Age incompatible")
        break
    except ValueError as ex:
        print(f"Erreur: {ex}")

print(f"Vous avez {age} ans")