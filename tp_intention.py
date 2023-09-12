# Créer la liste l1=[1,2,38,99,7,99,25,57]
# Créer des listes en intention pour
# Filtrer les impairs et les diviser par 2
# Filtrer les cos > 0.5
# Filtrer les fabs(tanh) < 0.98 et les * par 100
# Filtrer les nombre premiers et appliquer une racine carrée
import math
import my_module

l1=[1,2,38,99,7,99,25,57]
result = [x / 2 for x in l1 if x % 2 == 1]
print(result)

result = [x for x in l1 if math.cos(x) > 0.5]

result = [x * 100 for x in l1 if math.fabs(math.tanh(x)) < 0.98]
print(result)

result = [math.sqrt(x) for x in l1 if not(my_module.is_prime(x)) ]



