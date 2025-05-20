def factorielle(n: int) -> int:
    facto = 1
    for i in range(2, n + 1):
        facto *= i
    return facto

def is_palindrome(word: str) -> bool:
    is_palindrome = True
    for i in range(len(word) // 2):
        if word[i] != word[-i - 1]:
            is_palindrome = False
            break
    return is_palindrome


def is_prime(nb: int) -> bool:
    """
    Compute if nb is a prime number
    :param nb: the number
    :return: True if nb is a prime number
    """
    is_prime = True
    for i in range(2, int(nb ** 0.5) + 1):
        if nb % i == 0:
            is_prime = False
            break
    return is_prime

if __name__ == '__main__':
    result = factorielle(5)
    print(result)
    print(is_palindrome("radar"))
    print(is_prime(7))