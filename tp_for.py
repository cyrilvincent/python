# Porte tp_while en for

n = 5
facto = 1
for i in range(2, n+1):
    facto *= i
print(f"{n}!={facto}")

n = 10
fibo = 1
fibo2 = 0
for i in range(1, n):
    temp = fibo
    fibo = fibo + fibo2
    fibo2 = temp
print(f"F({n})={fibo}")

n = 1224
is_prime = True
for div in range(2, n):
    if n % div == 0:
        print("Non premier")
        is_prime = False
        break
if is_prime:
    print("Premier")
