import pickle

x = "toto"
y = [1,2,3]

with open("data/demo.pickle", "wb") as f:
    pickle.dump((x, y), f)

x = None
y = None

with open("data/demo.pickle", "rb") as f:
    x, y = pickle.load(f)

print(x, y)
