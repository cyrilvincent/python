import pickle
import json

x = list(range(1000))

# Save
with open("data/demo.pickle", "wb") as f:
    pickle.dump(x, f)

with open("data/demo.json", "w") as f:
    json.dump(x, f)

x = None

# Load
with open("data/demo.pickle", "rb") as f:
    x = pickle.load(f)

with open("data/demo.json", "r") as f:
    x = json.load(f)

print(x)



