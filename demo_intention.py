import tp_function

l = range(10)

result = []
for v in l:
    result.append(v ** 2)
print(result)

result = [x ** 2 for x in l]
print(result)

result = [x for x in l if x % 2 == 0]
print(result)

result = [x ** 2 for x in l if x % 2 == 0]
print(result)

def transform(x):
    if x % 2 == 0:
        return x * 2
    else:
        return x / 2

result = [transform(x) for x in l if tp_function.is_prime(x)]
print(result)



# Porter filter_even et filter_prime en liste en intention
# Puis monter au carré
# Ou appliquer la transformation suivante si x pair => * 2 si x impaire => / 2