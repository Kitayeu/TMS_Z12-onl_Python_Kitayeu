import threading
import time
import random

lock = threading.Lock()


class MyCounter:
    def __init__(self, count=None):
        self.count = 0 if count is None else count

    def add(self):
        with lock:
            current_count = self.count
            time_sleep = random.randint(1, 5)
            time.sleep(time_sleep)
            self.count = current_count + 1


def update_count(my_counter: MyCounter):
    my_counter.add()
    print(my_counter.count)


if __name__ == '__main__':
    my_counter = MyCounter()

    for i in range(5):
        torrent = threading.Thread(target=update_count, name=f"Torrent-{i}", args=(my_counter,))
        torrent.start()
