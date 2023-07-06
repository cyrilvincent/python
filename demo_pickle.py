import pickle

x = range(1000)

# Save
with open("data/demo.pickle", "wb") as f:
    pickle.dump(x, f)

x = None

# Load
with open("data/demo.pickle", "rb") as f:
    x = pickle.load(f)

print(x)



