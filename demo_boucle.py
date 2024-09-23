i = 0
while i < 10:
    print(f"Itération: {i}")
    i += 1
print("La suite")

for j in range(10):
    for i in range(2,10,2):
        print(f"Itération: {i}")
        if i == 8:
            continue
        print("toto")
    if j > 0:
        break

for i in range(10,-1,-1):
    print(i)