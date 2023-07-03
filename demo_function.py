def add(i,j):
    return i + j

res = add(2,3) # C like
print(res)

res = add(i=2, j=3) # By named parameter
print(res)

def is_even(nb):
    return nb % 2 == 0

print(is_even(7))
print(is_even(8))
