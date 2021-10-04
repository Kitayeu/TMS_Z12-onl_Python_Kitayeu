import asyncio
import requests

# generator function


def gen_f():
    for i in range(10):
        yield i


for j in gen_f():
    print(j)

# coroutines


def simple_coroutine():
    print('Start simple_coroutine')
    while True:
        val = (yield)
        print(val)


simple_cor = simple_coroutine()
print(next(simple_cor))
simple_cor.send('Hello')


def simple_coroutines():
    print('Start simple_coroutines')
    for i in range(10):
        val = (yield i)
        print(val)


sim_cor = simple_coroutines()
print(next(sim_cor))
sim_cor.send('a')
sim_cor.send('b')
sim_cor.send('c')
sim_cor.send('d')
sim_cor.send('e')
sim_cor.send('f')
sim_cor.send('g')
sim_cor.send('h')
sim_cor.send('i')

# asynchronous functions


async def my_async_func(val):
    print(val)


async def main():
    await my_async_func('Hi')


asyncio.run(main())


async def counting():
    print(3)
    await asyncio.sleep(0)
    print(2)
    await asyncio.sleep(0)
    print(1)
    await asyncio.sleep(0)
    print('start')
    await asyncio.sleep(0)


coroutine_counter = counting()
coroutine_counter.send(None)
coroutine_counter.send(None)
coroutine_counter.send(None)
coroutine_counter.send(None)


async def downloader(url=None):
    name = url.split('/')[-1]
    with open(f"D:/{name}", "wb") as d_file:
        request_execution = requests.get(url)
        d_file.write(request_execution.content)


image_downloader = downloader("https://beautiful-pictures.com/picture_one.jpg")
music_downloader = downloader("https://cool-music.com/artist/album/song.flac")

coroutines = [image_downloader, music_downloader]

while True:
    for coroutine in coroutines.copy():
        try:
            coroutine.send(None)
        except StopIteration:
            coroutines.remove(coroutine)
    if len(coroutines) == 0:
        break
