def add(i,j):
    return i + j

res = add(2,3) # C like
print(res)

res = add(i=2, j=3) # By named parameter
print(res)

def is_even(nb: int) -> bool:
    return nb % 2 == 0

def compute_distance(x1: float, y1:float, x2=0.0, y2:float=0) -> float:
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

print(is_even(7))
print(is_even(8))
res = compute_distance(1,2,3,4)
print(res)
print(compute_distance(1,2))
a = 1
b = 2
c = 3
d = 4
print(compute_distance(a,b,c,d))

