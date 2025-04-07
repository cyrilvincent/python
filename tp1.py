# Créer la variable current_year = 2025
# Saisir votre année de naissance
# Stocker dans une variable votre age + 1 et l'afficher
# Saisir un mot dans une variable
# Afficher les 3 1er caractères du mot
# Afficher tous les caractères sauf le 1er et le dernier : python => ytho

current_year = 2025
birth_year = input("Année de naissance : ")
birth_year = int(birth_year)
age = current_year - birth_year
print(f"Age : {age + 1}")

word = input("Saisir un mot : ")
print(word[:3])
print(word[1:-1])
n = 2
print(word[n:-n])

