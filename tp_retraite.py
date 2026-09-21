# https://www.lassuranceretraite.fr/portail-info/home/actif/age-depart/age-depart-retraite.html
# Saisir votre année de naissance
# Afficher votre age légale de départ à la retraite
# Afficher le nombre de trimestre necessaire pour avoir le taux plein
# Bonus : saisir votre nb trimestre actuel
# Afficher votre de age de départ à taux plein (ne peut pas être inférieur à l'age légale ou 67 ans)

birth = int(input("Année de naissance: "))

if birth <= 1965:
    age_depart = 62.75
elif birth == 1966:
    age_depart = 63.25
elif birth == 1967:
    age_depart = 63.5
elif birth == 1967:
    age_depart = 63.75
else:
    age_depart = 64

print(f"Age légal de départ à la retraite {age_depart} ans")

if birth <= 1965:
    nb_trim = 170
elif birth == 1965:
    nb_trim = 171
else:
    nb_trim = 172

print(f"Nb trimestre: {nb_trim}")

actual_nb_trim = int(input("Nb trimestre déjà cotisé: "))
trim = nb_trim - actual_nb_trim
year = trim / 4
age_tx_plein = 2026 - birth + year
if age_tx_plein > 67:
    age_tx_plein = 67
print(f"Age taux plein: {age_tx_plein}")
