l = [5,99,8,-1]
print(l)
l2 = [1,2,3,4]

print(l[1])
l.append(1000)
l.insert(2,0)
l.remove(1000)
print(l.count(99))
print(l)

for value2 in l2:
    l.append(value2)
print(l)

for value in l:
    print(value)

for index in range(len(l)):
    print(l[index])

i = 0
while i < len(l):
    print(l[i])
    i += 1

l3 = []
for value in l:
    l3.append(value)
print(l3)

def my_function(l :list[float]) -> list[float]:
    return []