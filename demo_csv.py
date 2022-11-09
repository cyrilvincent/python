import csv

f = open("data/house.csv")
reader = csv.DictReader(f)
for row in reader:
    surf = float(row["surface"])
    price = float(row["loyer"])
    print(surf, price)
# for line in f:
#     print(line.strip())

