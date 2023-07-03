# Saisir l'année en cours
# Saisir votre année de naissance
# Calculer votre age en fin d'année
# L'afficher, "joliment", la commande str(3.14) convertit un nombre en str
# Reprendre TP1 et afficher votre avec une chaine formatée
# Tester upper(), lower()

year = input("Saisir l'année en cours: ")
year = int(year)
birth = int(input("Saisir votre année de naissance: "))
age = year - birth
print(f"Vous avez {age} ans".upper())