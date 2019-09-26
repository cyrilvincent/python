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


with open("data/mesures.csv") as f:
    reader = csv.DictReader(f)
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

