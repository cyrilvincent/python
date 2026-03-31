l1 = [1,2,5,99,-5,77,25,30,-6,7.5]
print(len(l1))

l1.append(999)
l1.remove(77)
l1[0] = -1

for value in l1:
    print(value)

for i in range(len(l1)):
    print(f"Index: {i}, value: {l1[i]}")

total = 0
for value in l1:
    total += value
print(total)

def sum(list: list[float]) -> float:
    print("TP")