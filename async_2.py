import asyncio
import time

# simple asynchronous function


async def main():
    print('Hello        ')
    await asyncio.sleep(1)
    print('      World!')

asyncio.run(main())


# asynchronous function


async def follow(wait, meaning):
    await asyncio.sleep(wait)
    print(meaning)


async def launch():
    print(f"Started at {time.strftime('%X')}")

    await follow(1, 'Hello')
    await follow(2, 'World')

    print(f"Finished at {time.strftime('%X')}")

asyncio.run(launch())
# operation time of function is equal to amount of sleep


# asynchronous function with tasks


async def startup():
    task_1 = asyncio.create_task(follow(1, 'Hello'))
    task_2 = asyncio.create_task(follow(2, 'World'))

    print(f"Started at {time.strftime('%X')}")

    # Wait until both tasks are completed (must be equal to maximum task sleep time,
    # but less than sum of all sleep time)

    await task_1
    await task_2

    print(f"Finished at {time.strftime('%X')}")

asyncio.run(startup())
