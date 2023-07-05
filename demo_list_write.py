import random
from typing import List

def generate_random_list(length: int, max: int)-> List[int]:
    l = []
    for i in range(length):
        l.append(random.randint(0, max))
    return l

if __name__ == '__main__':
    l1 = generate_random_list(length=100, max=1000)
    print(l1)