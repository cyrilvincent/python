# Créer la variable year = 2020
# Saisir votre année de naissance
# Calculer votre age
# Afficher votre age dans une "jolie" chaine de caractères

year = 2020
birth = input("Merci de saisir votre année de naissance: ")
birthint = int(birth)
age = year - birthint
print(f"Vous avez {age} an(s)")