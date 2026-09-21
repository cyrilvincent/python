# for i in range(10,20,2):
#     # if i>15:
#     #     break
#     if i == 14:
#         continue
#     print(i)

nb = 10
sum = 1
for i in range(2, nb + 1):
    sum += i
print(sum)

# TP:
# Factorielle n! = n * (n-1)! 5! = 5*4*3*2 = 120 0! = 1! = 1
# Difficile : fibo(n) f(n) = f(n-1) * f(n-2) f(0)=0 f(1)= 1 https://fr.wikipedia.org/wiki/Suite_de_Fibonacci
# Bonus : Dire si nb est premier, tout nb >= 2 est premier sauf s'il possède un diviseur entre 2 et nb-1

nb = 5
facto = 1
for i in range(2, nb + 1):
    facto *= i
print(facto)

nb = 10
f0 = 0
f1 = 1
fibo = 0
for i in range(2, nb + 1):
    fibo = f0 + f1
    f0 = f1
    f1 = fibo
print(fibo)

nb = 7919
is_prime = True
if nb < 2:
    is_prime = False
else:
    for div in range(2, nb):
        if nb % div == 0:
            is_prime = False
            break
print(is_prime)

