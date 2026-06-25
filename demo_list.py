l = [1,2,3,99,4,5,98,6,7,8,9]
l.append(100)

sum = 0
for v in l:
    sum += v
print(sum)

sum = 0
for i in range(len(l)):
    sum += l[i]
print(sum)

sum = 0
for i, v in enumerate(l):
    sum += l[i]
print(sum)