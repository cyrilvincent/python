import asyncio


def toto():
    return 0

async def my_function_async():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

async def main():
    print("Main")
    await my_function_async()
    # await toto()

if __name__ == '__main__':
    # res = my_function_async()
    # print(res)
    asyncio.run(my_function_async())

