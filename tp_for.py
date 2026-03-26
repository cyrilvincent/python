# Refaire de tp_while mais avec un for
# Bonus : soit n=7 est que n est premier
# Un nb est premier ssi nb>0 il possède exactement 2 diviseurs 1 et n
# Tout nb>1 est premier sauf s'il possède un diviseur entre 2 et n-1

for i in range(0,100,2):
    print(i)

for i in range(100, 0, -6):
    print(i)

for i in range(17):
    print(2 ** i)

n = 6
result = 1
for i in range(2, n+1):
    result *= i
print(result)

n = 227
is_prime = True
if n <= 1:
    is_prime = False
else:
    for div in range(2, n):
        if n % div == 0:
            is_prime = False
            break
print(is_prime)
