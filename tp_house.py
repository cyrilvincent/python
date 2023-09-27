# python tp_house.py data/house/house.csv --csv
# Afficher: Ouverture de data/house/house.csv en mode csv: True

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path", help="path du fichier à ouvrir")
parser.add_argument("-c", "--csv", action="store_true", help="Indique si le ficher est un csv")
args = parser.parse_args()
print(f"Ouverture de {args.path} en mode csv: {args.csv}")


