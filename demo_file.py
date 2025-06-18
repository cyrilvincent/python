import csv

with open("data/house/house.csv") as f:
    # with open("data/house/out.csv", "w") as out:
    #     for row in f:
    #         out.write(row)

    reader = csv.DictReader(f, delimiter=",")
    for row in reader:
        loyer = int(row["loyer"])
        surface = int(row["surface"])
        print(loyer / surface)


