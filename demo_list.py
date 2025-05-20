l = [5,99,8,-2,55,52,2006,0,18,47]
print(l[1])
print(l[2:8])
l[2] = 98
l.append(100)
for x in l: # By value
    print(x)
for i in range(len(l)): # By index
    print(l[i])

l2 = []
for i in range(10):
    l2.append(i * 2)
print(l2)
