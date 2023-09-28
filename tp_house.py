# python tp_house.py data/house/house.csv --csv
# Afficher: Ouverture de data/house/house.csv en mode csv: True

import argparse
import pickle

parser = argparse.ArgumentParser()
parser.add_argument("path", help="path du fichier à ouvrir")
parser.add_argument("-c", "--csv", action="store_true", help="Indique si le ficher est un csv")
parser.add_argument("-p", "--pickle", action="store_true", help="Indique si le ficher est un pickle")

args = parser.parse_args()
print(f"Ouverture de {args.path} en mode csv: {args.csv}")

# Créer la fonction load(path) qui ouvre le fichier (house.csv)
# Et retourne un tuple Loyers, Surfaces
# load(args.path)
import csv
import sys
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

def load_pickle(path):
    with open(path, "rb") as f:
        loyers, surfaces = pickle.load(f)
        return loyers, surfaces

if __name__ == '__main__':
    if args.csv:
        loyers, surfaces = load_csv(args.path)
        with open("data/house/house.pickle", "wb") as f:
            pickle.dump((loyers, surfaces), f)
    # Créer l'argument -p --pickle
    # Créer la fonction load_pickle(path)
    # Faire le elif adéquat
    elif args.pickle:
        loyers, surfaces = load_pickle(args.path)
    else:
        print("Error, must specify file type with --csv")
        sys.exit(1)
    print(loyers)
    print(surfaces)
