from typing import List
import demo_list_write


def filter_even(l: List[int]) -> List[int]:
    res = []
    for val in l:
        if val % 2 == 0:
            res.append(val)
    return res


if __name__ == '__main__':
    l = [1,2,3,4,5,6,7,8,9,10]
    res = filter_even(l)
    print(res) # => [2,4,6,8,10]
    l = demo_list_write.generate_random_list(10, 100)
    print(l)
    res = filter_even(l)
    print(res)
    # Tester avec une list random