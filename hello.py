print("Hello World")
year = 2024
data = input("Saisir votre année de naissance: ")
data = int(data)
age = year - data
print(f"Vous avez {age:.2f} ans")

# < 1 an : BB
# < 12 ans : Enfant
# < 18 : Ado
# 64 : Actif
# 100 : Retraité
# Centenaire
