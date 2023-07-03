# Saisir l'année en cours
# Saisir votre année de naissance
# Calculer votre age en fin d'année
# L'afficher, "joliment", la commande str(3.14) convertit un nombre en str

year = input("Saisir l'année en cours: ")
year = int(year)
birth = int(input("Saisir votre année de naissance: "))
age = year - birth
print("Vous avez " + str(age) + " ans")