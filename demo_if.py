age = 30
wind = 20
toto = 1
if age % 2 == 0 and wind > 10:
    print("A")
    if toto == 1:
        print("C")

    else:
        print("D")
else:
    print("B")

condition =  age % 2 == 0 and wind > 10
if condition:
    print("OK")