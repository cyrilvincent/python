#Créer la variable year=2026
#Saisir votre prénom
#Afficher Bonjour + votre prénom en majuscule
#Saisir et stocker votre année de naissance
#Calculer et afficher votre age en fin d'année

year=2026
fname = input("Prénom: ")
print(f"Bonjour {fname.capitalize()}")

birth = int(input("Année de naissance: "))
age = year - birth
print(f"Vous avez {age} ans")