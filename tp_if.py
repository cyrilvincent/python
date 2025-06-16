# age = ??
# nb_trim = ??
# age < 1 : BB
# age < 12 : Enfant
# <18 : Ado
# > 18 Adulte
# > 60 : 3eme age

# > 16 and < 64 : actif
# > 67 : retraite taux plein
# https://www.lassuranceretraite.fr/portail-info/home/actif/age-depart/age-depart-retraite.html
# Calculer entre 64 et 67 votre age de depart à la retraite (172 - nb_trim) / 4 + 64

age = 65
nb_trim = 170

if age < 1:
    print("BB")
elif age < 12:
    print("Enfant")
elif age < 18:
    print("Ado")
else:
    print("Adulte")
if age >= 60:
    print("3eme age")
if 16 < age < 64:
    print("Actif")
elif age >= 67:
    print("Droit à la retraite à taux plein")
elif age >= 64:
    nb_trim_restant = (172 - nb_trim) / 4
    if nb_trim_restant <= 0:
        print("Droit à la retraite à taux plein")
    else:
        age_retraite = min(age + nb_trim_restant, 67)
        print(f"Vous aurez le taux plein à {age_retraite} an(s)")

