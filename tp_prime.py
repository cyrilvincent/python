n = 1223
is_prime = True
if n < 2:
    is_prime = False
else:
    for div in range(2, int(n ** 0.5) + 1):
        if n % div == 0:
            is_prime = False
            break
print(is_prime)