import json

with open("data/house/house.json") as f:
    dico = json.load(f)
    print(dico["loyer"].values())