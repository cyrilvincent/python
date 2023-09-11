# Saisir votre age
# Avec des if afficher votre classe d'age (nouveau né, enfant, ado, adulte, 3ème age, grand age)
# Afficher un compte à rebours 10 .. 0
# Afficher les multiples de 7 jusqu'à 100
# Saisir un chiffre et dire s'il est premier
#   Un nombre est premier (prime number) ssi il possède 2 diviseurs : 1 et lui-même
#   Tout nombre n est premier sauf s'il possède un diviseur entre 2 et n -1 sauf pour 2

age = int(input("Age : "))
if age < 1:
    print("BB")
elif age < 12:
    print("Enfant")
elif age < 18:
    print("Ado")
elif age < 60:
    print("Adulte")
elif age < 90:
    print("3ème age")
else:
    print("Grand age")

for i in range(10,-1,-1):
    print(i)

for i in range(7,100,7):
    print(i)

