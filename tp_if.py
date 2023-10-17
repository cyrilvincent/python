year = 2023
while True:
    try:
        birth = int(input("Année de naissance: "))
        break
    except ValueError as ex:
        print("Mauvaise saisie ", ex)
age = year - birth
print(f"Vous avez {age} ans")

if age < 10:
    print("Enfant")
elif age < 18:
    print("Ado")
elif age < 64:
    print("Actif")
else:
    print("Retraité")