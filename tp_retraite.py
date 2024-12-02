actual_year = 2024.75
birth_year = 1962.75
working_year = 1978.25
# Compter le nombre de trimestre en fin d'année (actual_year - working_year) * 4
legal_age = 64
# 64 ans il faut 172 trimestres
# Si < 172 : 172 - nb_trimestre = nb_trimestre à ajouter à 64
# Si > 67 ans c'est ok
# Afficher votre age
# Saisir vos infos : birth_year, working_year
# Afficher votre age de départ

actual_age = actual_year - birth_year
print(f"Vous avez {actual_age} ans")
if actual_age >= 67:
    print("Vous avez le droit d'être à la retraite")
else:
    nb_trimestre = (actual_year - working_year) * 4
    print(f"Vous avez {nb_trimestre} trimestres")
    if nb_trimestre >= 172 and actual_age >= 64:
        print("Vous avez le droit d'être à la retraite")
    else:
        if nb_trimestre > 172:
            nb_trimestre = 172
        retraite_age = 64 + (172 - nb_trimestre) / 4
        if retraite_age > 67:
            retraite_age = 67
        if actual_age >= retraite_age:
            print("Vous avez le droit d'être à la retraite")
        else:
            print(f"Vous aurez droit à la retraite à {retraite_age} ans")


