a = 1
b = a
a += 1
print(a, b)

a = [1,2]
b = a
a.append(3)
print(a, b)

a = [1,2]
b = a.copy() # list(a)
a.append(3)
print(a, b)

a = [1,2]
b = [1,2]
print(a == b, a is b)
a = b
print(a == b, a is b)

def toto(l: list):
    l.append("toto")
    return l

def toto2(l: list):
    return l.copy().append("toto")

def titi():
    res = [1,2]
    res.append(3)
    return res


l = [1,2,3]
l = toto(l)
print(l)
res = titi()
print(res)

# comprendre 
# créer la fonction filter_even(l:list[int]) -> list[int] ex: filter_even([1,2,3,4]) => [2,4]
# créer la focntion filter_prime (utiliser tp_function)