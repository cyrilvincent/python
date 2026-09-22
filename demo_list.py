l = [1,2,3,8,9,-1,99,0,66]
print(l[0])
print(l[1:5:2])
print(l[2:-2])
print(l[:5])
print(l[5:])

l.append(33)
l.insert(4,100)
l.remove(8)
print(l)
print(l.count(99))

for value in l:
    print(value)

for i in range(len(l)):
    print(l[i])

l = []
i = 0
while i < 10:
    l.append(i)
    i += 1
print(l)