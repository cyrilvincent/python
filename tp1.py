# Créer la variable year = 2024
# Saisir votre année de naissance
# Afficher votre age en fin d'année
# Saisir votre prénom espace nom dans la variable full_name
# full_name.index
# Créer la variable first_name qui contient uniquement le prénom
# Créer la variable last_name qui contient uniquement le nom
# Afficher

year = 2024
res = input("Année de naissance: ")
birth = int(res)
age = year - birth
print(f"Vous allez avoir {age} ans")
full_name = input("Saisir votre prenom nom: ")
space_index = full_name.index(" ")
first_name = full_name[:space_index]
last_name = full_name[space_index + 1:]
print(f"Prénom: {first_name.capitalize()}, nom: {last_name.capitalize()}")