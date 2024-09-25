# Lire data/house/house.csv
# Créer la liste loyers qui contient la liste des loyers
# Idem pour surface
# Calculer le loyer moyen et la surface moyenne
# Difficile: Créer la liste loyer_per_m2 = qui est la liste des loyer / surface
# Calculer le loyer par m2 moyen
# Bonus : Créer le ficher CSV avec 3 colonnes : loyer,surface,loyer_per_m2
# Bonus : OO, Fonctions
import csv
import pickle


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

def save(path, *args):
    l = list(args)
    with open(path, "wb") as f:
        pickle.dump(l, f)

def save_csv3(path, loyers, surfaces, loyers_per_m2):
    with open(path, "w") as f:
        f.write("loyer,surface,loyer_per_m2\n")
        for loyer,surface,loyer_per_m2 in zip(loyers, surfaces, loyers_per_m2):
            f.write(f"{loyer},{surface},{loyer_per_m2}\n")



if __name__ == '__main__':
    loyers, surfaces, loyers_per_m2 = load("data/house/house.csv")
    print(loyers_per_m2)
    print(sum(loyers) / len(loyers))
    print(sum(surfaces) / len(surfaces))
    print(sum(loyers_per_m2) / len(loyers_per_m2))
    save_csv3("data/house/house3.csv", loyers, surfaces, loyers_per_m2)
    # Sauvegarder les 3 listes avec pickle
    # Effacer les 3 listes
    # Recharcher les 3 listes
    with open("data/house/house.pickle", "wb") as f:
        pickle.dump((loyers, surfaces, loyers_per_m2), f)

    loyers = None
    surfaces = None
    loyers_per_m2 = None

    with open("data/house/house.pickle", "rb") as f:
        loyers, surfaces, loyers_per_m2 = pickle.load(f)
        print(loyers, surfaces, loyers_per_m2)