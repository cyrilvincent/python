l1 = [1,2,3,4,5,6,7,8,9,10]
print(len(l1))
l1.append(3)
print(l1)
for i in range(l1.count(3)):
    l1.remove(3)
print(l1)

def remove_all(nb: float, l:list[float]) -> list[float]:
    for i in range(l.count(nb)):
        l.remove(nb)
    return l

l1 = [1.,2,3,4,5,6,7,8,9,10,3]
l1 = remove_all(3, l1)
print(l1)

length = 0
for i in l1:
    length += 1
print(length)

def len(l: list[float]) -> int:
    total = 0
    for i in l:
        total += 1
    return total

def sum(l: list[float]) -> float:
    total = 0
    for i in l:
        total += i
    return total

def sum2(l: list[float]) -> float:
    total = 0
    for i in range(len(l)):
        total += l[i]
    return total

print(sum(l1))