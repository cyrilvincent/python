# Créer la variable year = 2024
# Saisir votre année de naissance
# Afficher votre age (en fin d'année)

year = 2024
stop = False
while not stop:
    try:
        birth = int(input("Année de naissance: "))
        age = year - birth
        print(f"Votre age est de {age} ans")
        stop = True
    except ValueError:
        print("Mauvaise saisie")