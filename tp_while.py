# Afficher de 0 à 99 inclus
# idem mais avec un pas de 2
# Saisir un nombre n et calculer n! = 5! = 5*4*3*2*1 = 120
# Saisir un mot et afficher si c'est un palindrome = "radar"
# Bonus : n est il premier, divisible que par 1 ET lui même

i = 0
while i < 99:
    print(i)
    i += 2

# n = int(input("n: "))
# i = 1
# facto = 1
# while i <= n:
#     facto = facto * i  # facto *= i
#     i += 1
# print(f"n!={facto}")

word = "radar"
i = 0
is_palindrome = True
while i < len(word) / 2 and is_palindrome:
    if word[i] != word[-i - 1]:
        is_palindrome = False
    i += 1
print(f"Palindrome: {is_palindrome}")

n = 1223
is_prime = True
div = 2
while div < n ** 0.5 and is_prime:
    if n % div == 0:
        is_prime = False
    div += 1
print(is_prime)
