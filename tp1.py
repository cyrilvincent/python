# Créer tp1.py
# Créer la variable current_year = 2021
# Saisir votre année de naissance
# Calculer votre age (au 31/12)
# L'afficher

current_year = 2021
birth_year_str = input("Saisir votre année de naissance: ")
birth_year_int = int(birth_year_str)
age = current_year - birth_year_int
print(f"Vous avez {age} ans")