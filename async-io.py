import asyncio


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    asyncio.create_task(say_after(1, "world"))
    await say_after(1, 'hello')
    print("...")


asyncio.run(main())
