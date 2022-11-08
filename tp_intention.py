# Filtrer une liste par nombre premier
# Idem puis les passer au carré
# Le faire avec filter + map ou [intention list]

import tp2

res = [x ** 2 for x in range(100) if tp2.is_prime(x)]
print(res)

res = list(filter(tp2.is_prime, range(100)))
res = list(map(lambda x: x **2, res))
print(res)
