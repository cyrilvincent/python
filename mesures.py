import csv

def findErrors(reader, delta = 1):
    difflist = ((int(row["T"]), abs(float(row["VT"]) - float(row["VM"]))) for row in reader)
    deltalist = (row for row in difflist if row[1] > delta)
    return deltalist


with open("data/mesures.csv") as f:
    reader = csv.DictReader(f)
    res = findErrors(reader)
    print(list(res))