x = int(input("x :"))
if x > 0:
    print("positif")
    if x % 2 == 0:
        print("Ok")
elif x < 0:
    print("négatif")
else:
    print("Nul")

if x > 0 and x % 2 == 0:
    print("Ok")

a = 2
b = 2
condition = a == b
if condition:
    print("a == b")


