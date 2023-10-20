import json

with open("data/house/house.json") as f:
    res = json.load(f)
    print(res)

# res["loyers"].append("toto")

with open("data/house/house2.json", "w") as f:
    json.dump(res, f, indent=4)
