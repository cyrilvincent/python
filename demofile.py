import csv

with open("data/house.csv") as f:
    reader = list(csv.DictReader(f))
    for row in reader:
        print(float(row["loyer"]) / float(row["surface"]))

l = [float(row["loyer"]) / float(row["surface"]) for row in reader]
loyersurface = sum(l) / len(l)

import pickle
with open("data/file.pickle", "wb") as f:
    pickle.dump(loyersurface, f)

loyersurface = None

with open("data/file.pickle", "rb") as f:
    loyersurface = pickle.load(f)

print(loyersurface)

print(l)
print(reader)

import json
s = json.dumps(reader)
print(s)
reader = json.loads(s)
print(reader)