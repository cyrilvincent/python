# Réécrire filter_even et filter_prime avec des listes en intentions
# Bonus filtrer les nombres pairs et premiers

import tp_function

l = [1, 2, 5, 99, 10, -1, 0, 99, 88, 41]
evens = [x for x in l if x % 2 == 0]
print(evens)
primes = [x for x in l if tp_function.is_prime(x)]
print(primes)
evens_primes = [x for x in l if tp_function.is_prime(x) and x % 2 == 0]
print(evens_primes)
evens_primes = [x for x in evens if tp_function.is_prime(x)]