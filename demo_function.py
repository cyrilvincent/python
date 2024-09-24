def add(x:float, y:float=0, z:float=0) -> float:
    return x + y + z

result = add(3,2)
print(result)

print(add(3,2))

def sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def add_multiple(a: float, *kargs) -> float:
    total = 0
    for p in kargs:
        total += p
    return total

print(sum(5))
# print(add(3,"toto"))
print(add_multiple())
