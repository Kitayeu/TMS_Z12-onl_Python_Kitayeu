import asyncio


async def factorial(name, number):
    counting = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}")
        await asyncio.sleep(1)
        counting *= i
    print(f"Task {name}: factorial({number}) = {counting}")
    return counting


async def main():
    """for a better display, make 3 requests at the same time"""
    data_list = await asyncio.gather(
        factorial('a', 2),
        factorial('b', 3),
        factorial('c', 4),
    )
    print(data_list)

asyncio.run(main())
