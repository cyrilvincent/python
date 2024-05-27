nb = int(input("Nb: "))
if nb % 2 == 0:
    print("Pair")
else:
    if nb % 3 == 0:
        print("Multiple 3")
    print("Impair")