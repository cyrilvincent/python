birth_year = 1972

if birth_year == 1961:
    nb_trimestre = 168
elif birth_year == 1962:
    nb_trimestre = 169
elif birth_year == 1963 or birth_year == 1964 or birth_year == 1965:
    nb_trimestre = 170
else:
    nb_trimestre = 172

print(nb_trimestre)

age_travail = 23
age_retraite = age_travail + nb_trimestre / 4
if age_retraite > 67:
    age_retraite = 67
print(f"Votre âge de départ à la retraite à taux plein est de {age_retraite} ans")