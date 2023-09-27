l1 = [0,1,2,7,5,99,6,-2,11,10]

# Map equivalent
res = [x + 1 for x in l1]
print(res)

# Filter equivalent
res = [x for x in l1 if x % 2 == 0]
print(res)

# Filter + map equivalent
res = [x + 1 for x in l1 if x % 2 == 0]
print(res)