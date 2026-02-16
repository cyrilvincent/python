# Saisir son année de naissance
# Afficher son age en fin d'année

year = input("Année de naissance: ")
year_int = int(year)
age = 2026 - year_int
print(f"Vous avez {age} ans")

if age < 18:
    print("Mineur")
else:
    print("Majeur")