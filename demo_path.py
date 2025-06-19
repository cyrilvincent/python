path = "data/cancer/data.csv"
print(path.split("/"))
print("/".join(path.split("/")[0:-1]))