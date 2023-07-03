# Saisir votre age
# Afficher votre catégorie d'age
# < 1 an : Nouveau né
# < 12 ans : Enfant
# < 18 ans : Ado
# < 64 ans : Actif
# < 90 : Retraité
# > 90 : Grand age

# Saisir un entier
# Afficher True si pair, False si impair

age = int(input("Votre age: "))
if age < 1:
    print("Nouveau né")
elif age < 12:
    print("Enfant")
elif age < 18 and age >= 12:
    print("Ado")
elif age < 64:
    print("Actif")
elif age < 90:
    print("Retraité")
else:
    print("Grand age")

is_even = age % 2 == 0
print(is_even)

