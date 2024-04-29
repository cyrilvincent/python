from typing import Dict, Set

dico: Dict[str, str] = {"007": "James Bond"}
dico["008"] = "Cyril Vincent"
del dico["008"]

for key in dico.keys():
    print(key, dico[key])

for value in dico.values():
    print(value)

for key, value in dico.items():
    print(key, value)

# myset: Set[str] = ["toto"]

