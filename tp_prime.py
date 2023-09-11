nb = int(input("Nb: "))
is_prime = False
if nb % 2 == 0:
    print("Pair")
else:
    print("Impair")
if nb >= 2:
    is_prime = True
    for div in range(2, int(nb ** 0.5) + 1):
        if nb % div == 0:
            is_prime = False
            break
    print(f"{nb} est il premier: {is_prime}")
