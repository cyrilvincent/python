l1 = [1.0, 2.0, 3.2, 4.4, 5.1]
l2 = [0.2, 0.3, 0.4, 0.1, 0.55]
l3 = range(5)

zipped = list(zip(l1, l2, l3))
print(zipped)

for t, c, x in list(zip(l1, l2, l3)):
    p = t * c + x
    print(p)