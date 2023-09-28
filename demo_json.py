import json
dico = {"l1": [1,2,3], "l2": [4,5,6]}
with open("data/demo.json", "w") as f:
    json.dump(dico, f)