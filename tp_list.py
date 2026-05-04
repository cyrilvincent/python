# l = [1,2,3,55,99,-2,4,8,-3,1000]
# for v in l:
#     print(v)
#
# for i in range(len(l)):
#     print(l[i])
#
# for i, v in enumerate(l):
#     print(i, v, l[i])
import time
import tp_function

def sum(l: list[float]) -> float:
    t0 = time.perf_counter_ns()
    total = 0
    for v in l:
        total += v
    tend = time.perf_counter_ns()
    print(f"Perf counter {tend-t0} ns")
    return total


def filter_even(l: list[int]) -> list[int]:
    result: list[int] = []
    for v in l:
        if v % 2 == 0:
            result.append(v)
    return result


def filter_prime(l: list[int]) -> list[int]:
    result: list[int] = []
    for v in l:
        if tp_function.is_prime(v):
            result.append(v)
    return result


def remove_all(l: list[float], value: float) -> list[float]:
    for _ in range(l.count(value)):
        l.remove(value)
    return l


if __name__ == '__main__':
    result = remove_all([1, 333, 2, 333, 3, 333], 333)

