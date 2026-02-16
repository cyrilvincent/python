l = [1,2,3,4,5]
print(l)

for i in l:
    print(i)

print(l[3])
print(l[1:4])

l.append(99)
l.insert(2, 98)
print(l)
l = l + [99]
print(l)
if 4 in l:
    l.remove(4)
l[0]=-1
print(l)
print(l.count(99))

# def example(l: list[int]) -> list[float]