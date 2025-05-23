import datetime
import time
import numpy as np
import tp_function

def send_email():
    print(f"Send email @ {datetime.datetime.now()}")
    time.sleep(2)

def get_rnd() -> int:
    print(f"Get rnd @ {datetime.datetime.now()}")
    time.sleep(1.5)
    return np.random.randint(0, 1000, 1)[0]

def is_prime(nb: int) -> bool:
    print(f"Get prime @ {datetime.datetime.now()}")
    time.sleep(1)
    return tp_function.is_prime(nb)

def test1():
    start = time.perf_counter()
    send_email()
    rnd = get_rnd()
    prime = is_prime(7)
    print(f"Result {rnd} {prime} @ {time.perf_counter() - start:.1f}s")

if __name__ == '__main__':
    test1()