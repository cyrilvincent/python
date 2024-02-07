import csv

with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        loyer = float(row["loyer"])
        surface = float(row["surface"])
        print(loyer / surface)

# Lire le fichier data/house/house.csv (il est dans le zip)
# Afficher les loyers
# Créer la liste loyers et ajouter tous les loyers dedans
# Idem pour surfaces
# Afficher le loyer min, max, moyen
# Idem pour surface
# Bonus idem pur loyer_per_m2