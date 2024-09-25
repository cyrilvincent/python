import csv

with open("data/house/house.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        # print(int(row["loyer"]) / int(row["surface"]))

# Lire data/house/house.csv
# Créer la liste loyers qui contient la liste des loyers
# Idem pour surface
# Calculer le loyer moyen et la surface moyenne
# Difficile: Créer la liste loyer_per_m2 = qui est la liste des loyer / surface
# Calculer le loyer par m2 moyen
# Bonus : Créer le ficher CSV avec 3 colonnes : loyer,surface,loyer_per_m2
# Bonus : OO, Fonctions