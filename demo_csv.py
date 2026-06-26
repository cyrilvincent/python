import csv

with open("data/house/house.csv") as f:  # Read par défaut "r"
    reader = csv.DictReader(f, delimiter=",")
    loyer_m2 = []
    for row in reader:
        loyer = int(row["loyer"])
        surface = int(row["surface"])
        loyer_m2.append(loyer / surface)
    print(loyer_m2)
    print(sum(loyer_m2)/len(loyer_m2))

    # TP Créer un nouveau module house.py
    # Créer la classe House avec les attributs loyer et surface
    # Créer la méthode load(path) -> list[House]