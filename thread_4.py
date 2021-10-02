import threading
import random
import time

from queue import LifoQueue


class MyCounter:
    def __init__(self):
        self.count = 0

    def add(self):
        current_count = self.count
        time_sleep = random.randint(1, 3)
        time.sleep(time_sleep)
        self.count = current_count + 1

    def dell(self):
        current_count = self.count
        time_sleep = random.randint(1, 3)
        time.sleep(time_sleep)
        self.count = current_count - 1


def add_counter(q: LifoQueue):
    print("Started add_counter")
    my_count = q.get()
    print(f"add_counter before {my_count.count}")
    my_count.add()
    print(f"add_counter after {my_count.count}")
    q.put(my_count)


def dell_counter(q: LifoQueue):
    print("Started dell_counter")
    my_count = q.get()
    print(f"dell_counter before {my_count.count}")
    my_count.dell()
    print(f"dell_counter after {my_count.count}")
    q.put(my_count)


if __name__ == '__main__':
    count = MyCounter()
    my_queue = LifoQueue()

    my_thread_1 = threading.Thread(target=add_counter, args=(my_queue,))
    my_thread_1.start()

    my_thread_2 = threading.Thread(target=dell_counter, args=(my_queue,))
    my_thread_2.start()

    my_queue.put(count)

    my_thread_2.join()
