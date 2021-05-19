import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Fichier à ouvrir")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbeux")
    parser.add_argument("-t", "--type", help="Type de fichier à ouvrir : csv, json, xml, xlsx")
    parser.add_argument("-s", "--separator", help="Séparateur des fichiers CSV")
    args = parser.parse_args()
    print(f"Loading {args.path}")
    if args.verbose:
        print(f"File type: {args.type}")
        if args.type == "csv":
            print(f"File separator: {args.separator}")
