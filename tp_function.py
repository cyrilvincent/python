# factorielle(n:int) -> int
# is_palindrome(word:str) -> bool
# is_prime(n: int) -> bool

def factorielle(n: int) -> int:
    """
    Factorielle
    :param n: parameter
    :return: n!
    """
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


def is_prime(n: int) -> bool:
    is_prime = True
    for div in range(2, int(n ** 0.5) + 1):
        if n % div == 0:
            is_prime = False
            break
    return is_prime

if __name__ == '__main__':
    print(is_palindrome("radar"))
    print(is_prime(7))
