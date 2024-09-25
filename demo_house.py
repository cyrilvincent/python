import csv

with open("data/house/house.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(int(row["loyer"]) / int(row["surface"]))