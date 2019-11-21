import csv
with open("data/house.csv") as f:
    reader = csv.DictReader(f)
    # for row in reader:
    #     print(int(row["loyer"]) / int(row["surface"]))
    res = [int(row["loyer"]) / int(row["surface"]) for row in reader]
    print(sum(res) / len(res))
    print(max(res))

with open("data/mesures.csv") as f:
    reader = csv.DictReader(f)
    res = [row for row in reader if abs(float(row["VT"]) - float(row["VM"])) > 1 ]
    print(res)