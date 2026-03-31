n = 5
facto = 1
for i in range(1,n+1):
    facto *= i
print(facto)

f0 = 0
f1 = 1
fibo = 0
for i in range(1, n):
    fibo = f0 + f1
    f0 = f1
    f1 = fibo
print(fibo)

n = 1223
is_prime = True
for div in range(2, n):
    if n % div == 0:
        is_prime = False
        break
print(is_prime)