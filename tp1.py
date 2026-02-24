# Créer la variable year = 2026
# Saisir votre année de naissance
# Afficher votre age en fin d'année

year = 2026

while True:
    try:
        birth = input("Année de naissance: ")
        birth = int(birth)
        if birth > year or birth < year - 130:
            raise ValueError("Date de naissance incompatible")
        age = year - birth
        print(f"Vous avez {age} ans")
        break
    except TypeError as err:
        print(err)
        print("Merci de resaisir votre age")
    except ValueError as err:
        print(err)
