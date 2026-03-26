# Créer la variable year = 2026
# Afficher le texte "L'année en cours est year"
# Créer la variable my_text = "Je suis en majuscule"
# Afficher my_text en majuscule # .upper()
# Saisir votre année de naissance en affichant un prompt compréhensible par un humain
# Caster votre année de naissance dans une nouvelle variable avec la fonction int()
# Afficher votre age en fin d'année

year = 2026
while True:
    try:
        print(f"L'année en cours est {year}.")
        my_text = "Je suis en majuscule"
        print(my_text.upper())
        birth_year_str = input("Saisir votre année de naissance: ")
        birth_year = int(birth_year_str)
        if birth_year > year or birth_year < 1900:
            raise ValueError("Impossible")
        age = year - birth_year
        print(f"Vous avez {age} ans")
        break
    except ValueError as ex:
        print(f"Erreur: {ex}")


