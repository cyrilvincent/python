f = open("data/house/house.csv")
# content = f.read()
# print(content)
for row in f:
    #print(row.strip())
    values = row.strip().split(",")
    print(values)

with open("data/toto.txt", "w") as f2:
    f2.write("Hello World!!")
