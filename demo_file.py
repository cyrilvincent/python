# f = open("data/house/house.csv")
# content = f.read()
# print(content)

import csv
import pickle
import datetime
import json

def load(path: str) -> tuple[list[float], list[float]]:
    loyers = []
    surfaces = []
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            loyer = float(row["loyer"])
            surface = float(row["surface"])
            loyers.append(loyer)
            surfaces.append(surface)
    return loyers, surfaces


def compute_loyer_per_m2(loyers: list[float], surfaces: list[float]) -> list[float]:
    loyer_per_m2 = []
    for i in range(len(loyers)):
        loyer_per_m2.append(loyers[i] / surfaces[i])
    return loyer_per_m2

def compute_loyer_per_m2_zip(loyers: list[float], surfaces: list[float]) -> list[float]:
    loyer_per_m2 = []
    for t in zip(loyers, surfaces):
        loyer_per_m2.append(t[0] / t[1])
    return loyer_per_m2

def compute_loyer_per_m2_intention(loyers: list[float], surfaces: list[float]) -> list[float]:
    return [loyer / surface for loyer, surface in zip(loyers, surfaces)]

# Faire la fonction load(path: str) tuple[list[float], list[float]]
# Faire la fonction compute_loyer_per_m2(loyers: list[float], surfaces: list[float) -> list[foat]
# afficher le résultat
# Sauvegarder le res en pickle, json, (xml) dans des fonctions
# Reloader le resultat depuis pickle, json, (xml)

loyers, surfaces = load("data/house/house.csv")
res = compute_loyer_per_m2(loyers, surfaces)
res = compute_loyer_per_m2_zip(loyers, surfaces)
res = compute_loyer_per_m2_intention(loyers, surfaces)
print(res)

def save_pickle(path: str, x):
    with open(path, "wb") as f:
        pickle.dump(x, f)

def load_pickle(path: str):
    with open(path, "rb") as f:
        return pickle.load(f)


def save_json(path: str, x):
    with open(path, "w") as f:
        json.dump(x, f)


def load_json(path: str):
    with open(path, "r") as f:
        return json.load(f)

def save(path: str, x, type: str):
    if type == "pickle":
        path += ".pickle"
        save_pickle(path, x)
    elif type == "json":
        path += ".json"
        save_json(path, x)
    else:
        raise ValueError(f"Bad type {type}")

def load(path: str):
    ext = path.split(".")[-1]
    if ext == "json":
        return load_json(path)
    elif ext == "pickle" or ext == "pkl":
        return load_pickle(path)
    else:
        raise ValueError(f"Unknown extension {ext}")

