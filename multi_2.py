from multiprocessing import Process, Queue
import os
import time


def proc_func(queue: Queue):
    number = queue.get()
    print(f'number {number}')
    print(f'parent process id {number}: {os.getppid()}')
    print(f'process id {number}: {os.getpid()}')
    time.sleep(20)


if __name__ == '__main__':
    q = Queue()

    for i in range(5):
        proc = Process(target=proc_func, args=(q,))
        proc.start()

    new_l = [x for x in range(1, 11) if x % 2 == 0]
    for x in new_l:
        q.put(x)
