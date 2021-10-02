import threading
import time
import random


def test_thread(number: int):
    print(f"Start {threading.current_thread().getName()}")
    time_sleep = random.randint(1, 10)
    print(f"Time sleep {time_sleep}")
    time.sleep(time_sleep)
    print(number ** 2)
    print(f"End {threading.current_thread().getName()}")


if __name__ == '__main__':
    for i in range(5):
        torrent = threading.Thread(target=test_thread, name=f"Torrent-{i}", args=(i, ))
        torrent.start()
