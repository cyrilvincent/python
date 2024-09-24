# Créer la variable year = 2024
# Saisir votre année de naissance
# Afficher votre age au 31/12

year = 2024
while True:
    birth = input("Année de naissance: ")
    try:
        birth = int(birth)
        age = year - birth
        print(f"Vous avez {age} ans")
        break
    except ValueError as ve:
        print(f"Erreur: {ve}")
