# Afficher les nombres multiples de 3 entre 0 et 100
# Soit n = entier >= 1, afficher n! 5! = 1*2*3*4*5 = 120
# + difficile, soit word = "radar" afficher si c'est un palindrome ?
# Bonus : soit n un entier >= 2, est-il premier?

i = 0
while i < 100:
    print(i)
    i += 3

n = 100
i = 2
facto = 1
while i <= n:
    facto *= i
    i += 1
print(f"{n}!={facto}")

is_prime = True
n = 1223
i = 2
while i <= n ** 0.5 and is_prime:
    if n % i == 0:
        is_prime = False
    i += 1
print(is_prime)

word = "radar"
i = 0
is_palindrome = True
while i <= len(word) / 2 and is_palindrome:
    if word[i] != word[-i - 1]:
        is_palindrome = False
    i += 1
print(is_palindrome)