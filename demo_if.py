couleur = "blanc"
vitesse = 21

if vitesse < 20 or couleur == "blanc":
    print("OK")
else:
    print("KO")

condition = vitesse < 20 or couleur == "blanc"
if condition:
    print("OK")
else:
    print("KO")


age = int(input("Age: "))
if age < 2:
    print("Bébé")
elif age < 12:
    print("Enfant")
elif age < 18:
    print("Ado")
elif age > 100:
    print("Centenaire")
elif age > 80:
    print("Vieux")
else:
    print("Adulte")