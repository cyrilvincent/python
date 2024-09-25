# Lire data/house/house.csv
# Créer la liste loyers qui contient la liste des loyers
# Idem pour surface
# Calculer le loyer moyen et la surface moyenne
# Difficile: Créer la liste loyer_per_m2 = qui est la liste des loyer / surface
# Calculer le loyer par m2 moyen
# Bonus : Créer le ficher CSV avec 3 colonnes : loyer,surface,loyer_per_m2
# Bonus : OO, Fonctions
import csv


def load(path: str) -> tuple[list[int], list[int], list[float]]:
    with open(path, "r") as f:
        loyers = []
        surfaces = []
        loyers_per_m2 = []
        reader = csv.DictReader(f)
        for row in reader:
            loyer = int(row["loyer"])
            surface = int(row["surface"])
            loyers.append(loyer)
            surfaces.append(surface)
            loyers_per_m2.append(loyer / surface)
        return loyers, surfaces, loyers_per_m2

if __name__ == '__main__':
    loyers, surfaces, loyers_per_m2 = load("data/house/house.csv")
    print(loyers_per_m2)
    print(sum(loyers) / len(loyers))
    print(sum(surfaces) / len(surfaces))
    print(sum(loyers_per_m2) / len(loyers_per_m2))