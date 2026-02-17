import csv

# with open("data/house/house.csv", "r") as f:
#     with open("data/house/house2.csv", "w") as w:
#         for row in f:
#             print(row.strip())
#             w.write(row)
#             row.split(",")
# print("End")

with open("data/house/house.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(int(row["loyer"])/int(row["surface"]))

# 1 load_csv(file_name) -> tuple[list[int], list[int]] # loyers et surfaces
# 2 for loyer, surface in zip(loyers, surfaces) Créer la liste loyer_m2
# 3 Afficher le loyer_m2 moyen