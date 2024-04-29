print("Hello World!")

s = input("Saisir x: ")
x = int(s)

if x > 1:
    for div in range(2, x):
        if x % div == 0:
            print("Non premier")
            break
    print("Premier")
