import pickle

x = "Hello World!"
y = [1,2,3,4]

with open("data/hello.pickle", "wb") as f:
    pickle.dump((x,y), f)

x = None

with open("data/hello.pickle", "rb") as f:
    x, y = pickle.load(f)
    print(x, y)

