import argparse
import os
import csv
import sys


class HouseCsv:

    def __init__(self, path, separator=","):
        self.path = path
        self.separator = separator
        self.loyers = []
        self.surfaces = []
        self.loyers_per_m2 = []

    def load(self):
        with open(self.path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                loyer = int(row["loyer"])
                surface = int(row["surface"])
                self.loyers.append(loyer)
                self.surfaces.append(surface)
                self.loyers_per_m2.append(loyer / surface)

    def min_max_avg(self, l):
        min = max = l[0]
        sum = 0
        for value in l:
            sum += value
            if value < min:
                min = value
            elif value > max:
                max = value
        return min, max, sum / len(l)

    def compute_loyers(self):
        return self.min_max_avg(self.loyers)

    def compute_surfaces(self):
        return self.min_max_avg(self.surfaces)

    def compute_loyers_per_m2(self):
        return self.min_max_avg(self.loyers_per_m2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Fichier à ouvrir")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbeux")
    parser.add_argument("-t", "--type", help="Type de fichier à ouvrir : csv, json, xml, xlsx")
    parser.add_argument("-s", "--separator", help="Séparateur des fichiers CSV")
    args = parser.parse_args()
    print(f"Loading {args.path}")
    if args.verbose:
        print(f"Current directory {os.getcwd()}")
        print(f"File type: {args.type}")
        if args.type == "csv":
            print(f"File separator: {args.separator}")
    if args.type == "csv":
        housecsv = HouseCsv(args.path, args.separator)
        housecsv.load()
        if args.verbose:
            min, max, avg = housecsv.compute_loyers()
            print(f"Loyers min: {min:.0f}, max: {max:.0f}, avg: {avg:.1f}")
            min, max, avg = housecsv.compute_surfaces()
            print(f"Surfaces min: {min:.0f}, max: {max:.0f}, avg: {avg:.1f}")
            min, max, avg = housecsv.compute_loyers_per_m2()
            print(f"Loyers par m² min: {min:.0f}, max: {max:.0f}, avg: {avg:.1f}")
        else:
            _, _, avg = housecsv.compute_loyers_per_m2()
            print(avg)
    else:
        print("ERROR bad type")
        sys.exit(1)

    # Charger le fichier path et créer les listes loyers et surfaces
    # Rendez le séparateur paramétrable parse(path, separator)
    # Uniquement pour --type csv
    # Si verbose afficher min, max, moyenne des surfaces, loyers, loyers par m²
    # Si non verbose moyenne des loyers par m²
