import datetime
import time
import numpy as np
import tp_function
import asyncio

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

async def send_email_async():
    print(f"Send email @ {datetime.datetime.now()}")
    await asyncio.sleep(2)

async def get_rnd_async() -> int:
    print(f"Get rnd @ {datetime.datetime.now()}")
    await asyncio.sleep(1.5)
    return np.random.randint(0, 1000, 1)[0]

async def is_prime_async(nb: int) -> bool:
    print(f"Get prime @ {datetime.datetime.now()}")
    await asyncio.sleep(1)
    return tp_function.is_prime(nb)

def test1():
    start = time.perf_counter()
    send_email()
    rnd = get_rnd()
    prime = is_prime(7)
    print(f"Result {rnd} {prime} @ {time.perf_counter() - start:.1f}s")

async def test2():
    start = time.perf_counter()
    await send_email_async()
    rnd = await get_rnd_async()
    prime = await is_prime_async(7)
    print(f"Result {rnd} {prime} @ {time.perf_counter() - start:.1f}s")

async def test3():
    start = time.perf_counter()
    task = asyncio.create_task(send_email_async())
    rndTask = asyncio.create_task(get_rnd_async())
    primeTask = asyncio.create_task(is_prime_async(7))
    rnd = await rndTask
    prime = await primeTask
    print(f"Result {rnd} {prime} @ {time.perf_counter() - start:.1f}s")

if __name__ == '__main__':
    test1()
    asyncio.run(test2())
    asyncio.run(test3())