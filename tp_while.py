# Créer une boucle de 0 à 10 non inclus
# Créer un compte à rebourd de 100 à 0 inclus avec un pas de -2
# Calculer la factorielle de n : n=5, 5! = 5*4*3*2*1
# Bonus: Fibonacci (3 variables)
# Bonus difficile : Soit n=7 est ce que n est premier?  divisible uniquement par 1 et lui-même
# Tout nombre > 1 est premier sauf s'il possède un diviseur entre 2 et n-1

n = 5
i = 2
facto = 1
while i <= n:
    facto *= i
    i += 1
print(f"{n}!={facto}")

n = 10
i = 1
fibo = 1
fibo2 = 0
while i < n:
    temp = fibo
    fibo = fibo + fibo2
    fibo2 = temp
    i += 1
print(f"F({n})={fibo}")

n = 1223
div = 2
if n < 2:
    print("Non premier")
else:
    while div < n:
        if n % div == 0:
            print("Non premier")
            break
        div += 1
    if div == n:
        print("Premier")