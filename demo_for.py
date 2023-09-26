for i in range(0, 100, 2):
    print(i)

for i in range(10, -1, -1):
    print(i)

n = 5
res = 1
for i in range(1, n + 1):
    res *= i
print(res)

n = 2
is_prime = True
if n<2:
    is_prime = False
else:
    for div in range(2, n):
        if n % div == 0:
            is_prime = False
            break
    print(is_prime)