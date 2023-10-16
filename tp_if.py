year = 2023
birth = int(input("Année de naissance: "))
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