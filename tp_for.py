# for i in range(0, 100, 2):
#     print(i)

n = 5
facto = 1
for i in range(2, n+1):
    facto *= i
print(facto)

word = "radar"
is_palindrome = True
for i in range(len(word) // 2):
    if word[i] != word[-i - 1]:
        is_palindrome = False
        break
print(is_palindrome)

n = 1223
is_prime = True
for div in range(2, int(n ** 0.5) + 1):
    if n % div == 0:
        is_prime = False
        break

print(is_prime)

