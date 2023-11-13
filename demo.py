import logging as log

i = 3.14116
s = "toto"
print(type(i))
print("Affichage : " + str(i) + " " + s)
print(f"Affichage : {i:.2f} {s}")

for i in range(10,-1,-1):
    print(i)

def add(x:int, y=0., z=0.) -> float:
    return x + y + z


