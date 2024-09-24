import tp3

l = [1,2,5,9,99,-1,0,8,14,50]

# Map
res = [x * 2 for x in l]
print(res)

# Filter
res = [x for x in l if x % 2 == 0]
print(res)

# Filter + Map
res = [x * 2 for x in l if x % 2 == 0]
print(res)