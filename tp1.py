#Demander à l'utilisteur de saisir son prénom
#Afficher le prénom en majuscule
#Afficher le nombre de caractère du prénom
#Créer la variable year = 2026
#Saisir votre année de naissance
#Afficher votre age en fin d'année

# prenom = input("Prénom: ")
# print(prenom.upper())
# print(len(prenom))

while True:
    try:
        year=2026
        birth = input("Année de naissance: ")
        birth2 = int(birth)
        age = year - birth2
        if age < 0:
            raise ValueError("Age < 0")
        print(f"Vous avez {age} ans")
        break
    except ValueError as ex:
        print(f"Erreur {ex}")

# birth n'est pas un nb
# age ne peut pas être < 0