import json

config = {
    "name": "Formation Python",
    "copyright": "(C) CEA 2025",
    "version": "0.0.1",
    "nb_user": 10,
    "instruments": [
        {
            "id": 1,
            "name": "multimeter 1",
            "ip": "127.0.0.1",
            "type": "multimetre",
            "measure_types": ["voltmeter", "ampermeter"],
            "color": "black"
        },
        {
            "id": 2,
            "name": "multimeter 2",
            "ip": "127.0.0.2",
            "type": "multimetre",
            "measure_types": ["voltmeter", "ampermeter"],
            "color": None
        }
    ]
}


if __name__ == '__main__':
    print(config["name"])
    print(config["instruments"][0]["name"])
    for instrument in config["instruments"]:
        print(instrument["ip"])


# Dans un fichier main.py afficher le name du programme + version + copyright
# Dans __name__ == '__main__': faire une boucle sur les intruments et afficher les names
# idem mais afficher toues les measure_types

    for instrument in config["instruments"]:
        for measure_type in instrument["measure_types"]:
            print(measure_type)

with open("data/equipments.json", "w") as f:
    json.dump(config, f, indent="\t")


with open("data/equipments.json", "r") as f:
    dico = json.load(f)
    print(config["name"])
