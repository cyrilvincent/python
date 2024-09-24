l = [5,7,99,8,-2]
print(l)

l2 = l[:3]
print(l)

for value in l:
    print(value)

l.append(100)
print(l)
l.insert(2,999)
print(l)
l.remove(99)

l.append(100)
print(l)
print(l.index(100))
print(l.count(100))
for i in range(l.count(100)):
    l.remove(100)

def ma_fonction(l:list[int]):
    pass




