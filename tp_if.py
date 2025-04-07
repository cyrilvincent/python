# Saisir age
# Afficher votre catégorie d'age
# < 1 Nourrisson
# < 12 Enfant
# < 18 Ado
# < 62 Actif
# Retraité

age = int(input("Saisir age: "))
if age < 1:
    print("Nourrisson")
elif age < 12:
    print("Enfant")
elif age < 18:
    print("Ado")
elif age < 62:
    print("Actif")
else:
    print("Retraité")