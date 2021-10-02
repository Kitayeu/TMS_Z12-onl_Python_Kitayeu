import threading
import time
import random


def test_thread(number: int):
    print(f"Start {threading.current_thread().getName()}")
    time_sleep = random.randint(1, 10)
    print(f"Time sleep {time_sleep}")
    time.sleep(time_sleep)
    print(number)
    print(f"End {threading.current_thread().getName()}")


class ThreadTest(threading.Thread):
    def __init__(self, number: int, func):
        threading.Thread.__init__(self)
        self.number = number
        self.func = func

    def run(self) -> None:
        self.func(self.number)


if __name__ == '__main__':
    for i in range(5):
        torrent = ThreadTest(i, test_thread)
        torrent.setName(f"Class-Torrent-{i}")
        torrent.start()
