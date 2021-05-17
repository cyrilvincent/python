# Saisir votre année de naissance et calculer votre age (copier coller tp1)
# Afficher votre catégorie d'age (nourrisson <1, enfant < 11, ado < 18, adulte > 18)
# Afficher votre status (18-62) : actif, > 62 retraité
current_year = 2021
birth_year_str = input("Saisir votre année de naissance: ")
birth_year_int = int(birth_year_str)
age = current_year - birth_year_int
if age < 1:
    print("Nourisson")
elif age < 11:
    print("Enfant")
elif age < 18:
    print("Ado")
else:
    print("Adulte")
    if age < 62:
        print("Actif")
    else:
        print("Retraité")
