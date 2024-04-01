from multiprocessing import Pipe, Queue, Process
from threading import Thread
import time
import codecs

def process_main(main1, main2):
    def read_n_send():
        stdin = open(0)
        for line in stdin:
            main1.send(line)
            print(f'{time.time():.4f}s: main sent {line}', end='')

    def get_n_print():
        while main2.poll(timeout=15):
            message = main2.recv()
            print(f'{time.time():.4f}s: {message}', end='')

    t1 = Thread(target=read_n_send, args=())
    t2 = Thread(target=get_n_print, args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()

def process_a(a1, a2, queue):
    def receive():
        while a1.poll(timeout=15):
            message = a1.recv()
            message = message.lower()
            queue.put(message)

    def sending():
        while not queue.empty():
            message = queue.get()
            a2.send(message)
            print(f'{time.time():.4f}s: A sent {message}', end='')
            time.sleep(5)

    t1 = Thread(target=receive, args=())
    t1.start()
    while t1.is_alive():
        t2 = Thread(target=sending, args=())
        t2.start()
        t2.join()
    t1.join()

def process_b(b1, b2):
    while b1.poll(timeout=16):
        message = b1.recv()
        enc_message = codecs.encode(message, 'rot_13')
        b2.send(enc_message)


if __name__ == '__main__':
    queue = Queue()
    (a1, main1) = Pipe(duplex=False)
    (b1, a2) = Pipe(duplex=False)
    (main2, b2) = Pipe(duplex=False)

    p_main = Process(target=process_main, args=(main1, main2,))
    p_a = Process(target=process_a, args=(a1, a2, queue,))
    p_b = Process(target=process_b, args=(b1, b2,))
    p_main.start()
    p_a.start()
    p_b.start()
    p_main.join()
    p_a.join()
    p_b.join()
