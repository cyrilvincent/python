import math
import tp_function as tp

l1 = [1,2,5,99,-5,77,25,30,-6,7]

# Traitement
result = [x * 2 for x in l1]

# result = []
# for x in l1:
#     result.append(x * 2)
print(result)

# Filter
result = [x for x in l1 if x % 2 == 0]
print(result)

def complex(x):
    if x < 10:
        return 0
    else:
        return x * math.sin(x)

# Traitement + Filtre
result = [x * 2 for x in l1 if x % 2 == 0]
print(result)

# Traitement + Filtre
result = [complex(x) for x in l1 if tp.is_prime(x)]
print(result)

# Filtrer les nombres pairs et / 2
# Filtrer les nb premier et appliquer un x.tanh
result = [x / 2 for x in l1 if x % 2 == 0]
result = [math.tanh(x) for x in l1 if tp.is_prime(x)]