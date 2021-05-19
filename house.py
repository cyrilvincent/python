import argparse
import os

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
    # Charger le fichier path et créer les listes loyers et surfaces
    # Rendez le séparateur paramétrable parse(path, separator)
    # Uniquement pour --type csv
    # Si verbose afficher min, max, moyenne des surfaces, loyers, loyers par m²
    # Si non verbose moyenne des loyers par m²
