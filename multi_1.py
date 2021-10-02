from multiprocessing import Process
import os
import time


def proc_func(number):
    print(f'number {number}')
    print(f'parent process id {number}: {os.getppid()}')
    print(f'process id {number}: {os.getpid()}')
    time.sleep(20)


if __name__ == '__main__':
    for i in range(5):
        proc = Process(target=proc_func, args=(i,))
        proc.start()
