l = [1,2,5,99,10,-1,0,99,88,41]
print(len(l))
print(l[0], l[-1])
print(l[2:5])
print(l[1:-1])
n = 2
print(l[n:-n])
l.remove(99)
print(l)

for value in l:
    print(value)

l = range(10)
for i in l:
    print(i)

