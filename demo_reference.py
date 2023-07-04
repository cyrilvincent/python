# By value
a = 1
b = a
a += 1
print(f"a={a} b={b}")

# By reference
l1 = [1,2]
l2 = l1
l1.append(3)
print(f"l1={l1} l2={l2}")

# Clone
l1 = [1,2]
l2 = list(l1)
l1.append(3)
print(f"l1={l1} l2={l2}")

def inc(x: int):
    return x + 1