import time
from threading import Thread
from multiprocessing import Process

def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def sync_time():
    start = time.time()
    for i in range(10):
        fibonacci(36)
    return time.time() - start

def thr_time():
    start = time.time()
    threads = [Thread(target=fibonacci, args=(36,)) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return time.time() - start

def proc_time():
    start = time.time()
    processes = [Process(target=fibonacci, args=(36,)) for _ in range(10)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    return time.time() - start


if __name__ == '__main__':
    with open('4.1.txt', 'w') as f:
        f.write(f"10-wise synchronous time: {sync_time()} \n")
        f.write(f"10-wise threading time: {thr_time()} \n")
        f.write(f"10-wise process time: {proc_time()}")
