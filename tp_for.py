# Porter tp_while en for

sum = 0
for i in range(11):
    sum += i
print(sum)

for i in range(11):
    for j in range(11):
        print(f"{i}x{j}={i * j}")

n = 5
result = 1
for i in range(2, n + 1):
    result *= i
print(f"{n}!={result}")

n = 10
f0 = 0
f1 = 1
result = 0
for i in range(2, n+1):
    result = f0 + f1
    f0 = f1
    f1 = result
print(f"F({n})={result}")

n=7919
is_prime = True
if n < 2:
    is_prime = False
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break
print(is_prime)

