import asyncio
import time


async def main():
    print("aaeea")
    task = asyncio.create_task(foo("Henloo"))
    await task
    print("eeaeae")


async def foo(text):
    print(text)
    time.sleep(1)


if __name__ == '__main__':
    asyncio.run(main())
