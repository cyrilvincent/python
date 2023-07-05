import random
from typing import List

print(random.random())
print(random.randint(0, 100))

def generate_random_list(length: int, max: int)-> List[int]:
    l = []
    for i in range(length):
        l.append(random.random(0, max))
    return l

l1 = generate_random_list(length=100, max=1000)
print(l1)