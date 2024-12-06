import pickle

data = 3.14

with open("data/out.pickle", "wb") as f:
    pickle.dump(data, f)

data = None

with open("data/out.pickle", "rb") as f:
    data = pickle.load(f)
    print(data)