from multiprocessing import Process
import os
import time

def sqr(n):
    print(n)
    for i in range(100):
        i ** 2
        time.sleep(0.1)

if __name__ == '__main__':
    processes = []
    num_processes = os.cpu_count()

    # create the processes
    for i in range(num_processes):
        p = Process(target=sqr, args=(20))
        processes.append(p)

    # start the processes
    for p in processes:
        p.start()

    # joining - blocks the main programn until all processes are done
    for p in processes:
        p.join()
    print('processes ended')
