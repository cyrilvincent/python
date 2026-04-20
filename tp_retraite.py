# D'après https://www.lassuranceretraite.fr/portail-info/home/actif/age-depart/age-depart-retraite.html
# > 1er septembre 2026
# Saisir votre année de naissance
# Calculer votre age légal de départ à la retraite
# Calculer le nb de trimestre à cotiser pour avoir une retraite à taux plein
# Saisir votre age de début de cotisation
# En supposant que vous ne serez jamais au chomage et jamais enceinte calculer votre age de départ à la retraite
# A 67 ans vous êtes à taux plein

birth_year = 1972

if birth_year <= 1964:
    age_legal = 62
elif birth_year <= 1968:
    age_legal = 63
else:
    age_legal = 64

print(f"Age légal: {age_legal}")

if birth_year <= 1965:
    nb_trimestre = 170
elif birth_year <= 1966:
    nb_trimestre = 171
else:
    nb_trimestre = 172

age_cotisation = 23

age_depart = age_cotisation + nb_trimestre / 4
if age_depart > 67:
    age_depart = 67

print(f"Age départ: {age_depart}")

