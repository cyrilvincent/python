# l1 = [1,5,9,12]
l1 = list(range(7,100,7))
l1.append(99)
print(l1)

total = 1
for value in l1:
    total = total * value
print(total)
