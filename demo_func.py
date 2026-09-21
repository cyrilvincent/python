def add(i: float, j: float) -> float:
    return i + j

titi = add
print(titi(2,3))

print(add(2, 3))
result = add(2, 3)
print(result)
print(add(j=2, i=3))
print(add(2, 3.14))

def addn(*kargs) -> int:
    sum = 0
    for k in kargs:
        sum += k
    return sum

print(addn(1,2,3,4))

def toto(**kwargs):
    for w in kwargs:
        print(w)

toto(a="a",b="b",c=2,d=3)

f = lambda x, y: x + y