# Saisir votre age
# Si < 1 = Afficher BB
# Si < 10 = enfant
# < 18 = Ado
# < 64 = Adulte
# < 90 = Retraité
# Au delà = Grand age

age = int(input("Age: "))
if age < 1:
    print("BB")
elif age <= 10:
    print("Enfant")
elif age < 18:
    print("Ado")
elif age < 64:
    print("Adulte")
elif age < 90:
    print("Retraité")
else:
    print("Grand age")

