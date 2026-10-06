i = 1
total = 0
while i < 10:
    total += i
    i += 1
print(total)

n = 5
facto = 1
for i in range(2, n+1):
    facto = facto * i
print(f"{n}!={facto}")

f0 = 0
f1 = 1
fibo = 1
n = 10
for i in range(2, n + 1):
    fibo = f0 + f1
    f0 = f1
    f1 = fibo
print(fibo)
