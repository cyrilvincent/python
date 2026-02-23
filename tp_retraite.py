nb_trimestre = 122
year_birth = 1972
year = 2026
age = year - year_birth
# Si née après 1966
# Si >= 172 trimestres ET 62 ans = taux plein
# Si 67 ans = taux plein
# Si < 172 trimestres
# Age de départ à taux plein (172-nb_trimestre)/4+age

if age >= 67:
    print("Taux plein")
elif age < 62:
    print("Faut encore travailler")
if age < 67:
    remaining = (172 - nb_trimestre) / 4
    age_depart = age + remaining
    if age_depart > 67:
        age_depart = 67
    print(f"Age de départ à la retraite: {age_depart}")

