# Reprendre le TP1
# age = ??
# < 1 : BB
# <12 : Enfant
# <18 : Ado
# <64 : Actif
# >100 : Centenaire

# nb_quarter = ??
# Rappel : 64 ans ET 172 quarters

age = 65
nb_quarter = 168
if age<1:
    print("BB")
elif age < 12:
    print("Enfant")
elif age < 18:
    print("Ado")
elif age < 64:
    print("Actif")
elif age < 67:
    if nb_quarter >= 172:
        print("Retraité à taux plein")
    else:
        nb_future_quarter = 172 - nb_quarter
        print(f"Il vous reste {nb_future_quarter} trimestre(s) à travailler")
elif age < 100:
    print("Retraité")
else:
    print("Centenaire")