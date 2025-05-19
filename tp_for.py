n = 5
facto = 1
for i in range(2,n+1):
    facto *= i
print(f"{n}!={facto}")

is_prime = True
n = 1223
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        is_prime = False
        break
print(is_prime)

word = "radar"
is_palindrome = True
for i in range(len(word) // 2):
    if word[i] != word[-i - 1]:
        is_palindrome = False
        break
print(is_palindrome)