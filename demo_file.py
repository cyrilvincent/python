with open("data/house/house.csv", mode="r") as f:
    # content = f.read()
    # print(content)

    for row in f:
        print(row, end="")

with open("data/house/test.csv", mode="a", encoding="utf-8") as w:
    w.write("J'ai ajouté")
    w.close()

with open("data/house/house.csv", mode="r") as f:
    with open("data/house/house2.csv", mode="w") as g:
        for row in f:
            g.write(row)

import csv
with open("data/house/house.csv", mode="r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

with open("data/house/house.csv", mode="r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        for key in row.keys():
            print(key, row[key])

with open("data/house/house.csv", mode="r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(int(row["loyer"]) / int(row["surface"]))