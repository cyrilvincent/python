import csv
import pickle
import jsonpickle

def findErrors(reader, delta = 1):
    difflist = (
                (int(row["T"]), abs(float(row["VT"]) - float(row["VM"])))
                    for row in reader
                )
    deltalist = (row for row in difflist if row[1] > delta)
    return deltalist

import matplotlib.pyplot as plt
with open("data/mesures.csv") as f:
    reader = list(csv.DictReader(f))
    res = findErrors(reader)
    res = list(res)
    with open("data/result.pickle", "wb") as g:
        pickle.dump(res, g)
    res = None
    with open("data/result.pickle", "rb") as g:
        res = pickle.load(g)
    print(res)
    s = jsonpickle.encode(res, unpicklable = False)
    print(s)
    vm = [float(row["VM"]) for row in reader]
    diff = [float(row["VM"]) - float(row["VT"]) for row in reader]
    plt.subplot(211)
    plt.plot(range(len(vm)), vm)
    plt.subplot(212)
    plt.plot(range(len(diff)), diff)
    plt.savefig("data/plot.png")
    plt.show()


