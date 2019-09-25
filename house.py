import sys
import csv
with open("data/house.csv") as f:
    reader = csv.DictReader(f)
    l = [int(row["loyer"]) / int(row["surface"]) for row in reader]
    print(sum(l)/len(l))
