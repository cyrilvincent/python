import pickle

x = "toto"
with open("data/toto.pkl", "wb") as f:
    pickle.dump(x, f)

x = None
with open("data/toto.pkl", "rb") as f:
    x = pickle.load(f)
    print(x)
