with open("data/house/house.csv") as f:  # Read par défaut "r"
    with open("data/house/house2.csv", "w") as g:
        i = 0
        for row in f:
            if i % 2 == 0:
                g.write(row)
            i+=1
