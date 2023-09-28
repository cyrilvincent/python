# python tp_house.py data/house/house.csv --csv
# Afficher: Ouverture de data/house/house.csv en mode csv: True

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path", help="path du fichier à ouvrir")
parser.add_argument("-c", "--csv", action="store_true", help="Indique si le ficher est un csv")
args = parser.parse_args()
print(f"Ouverture de {args.path} en mode csv: {args.csv}")

# Créer la fonction load(path) qui ouvre le fichier (house.csv)
# Et retourne un tuple Loyers, Surfaces
# load(args.path)
import csv
def load_csv(path):
    with open(path) as f:
        reader = csv.DictReader(f)
        loyers = []
        surfaces = []
        for row in reader:
            loyer = float(row["loyer"])
            surface = float(row["surface"])
            loyers.append(loyer)
            surfaces.append(surface)
        return loyers, surfaces

if __name__ == '__main__':
    loyers, surfaces = load_csv("data/house/house.csv")
    print(loyers)
    print(surfaces)
