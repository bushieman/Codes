from queue import Queue
from threading import Thread, Lock, current_thread

q = Queue()

q.put(1)
q.put(2)
q.put(3)

# gets the first item in the queue and removes it from the queue
first = q.get()

# other queue methods
q.empty()
q.task_done() # 
q.join() # lock and wait for elements processing



def worker(q, lock):
    while True:
        value = q.get()
        # processing...
        with lock:
            print(f'in {current_thread().name} got {value}')
        q.task_done()


if __name__ == '__name__':
    q = Queue()
    num_threads = 10
    lock = Lock()
    for _ in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon = True
        thread.start()

    for i in range(1, 21):
        q.put(i)

    q.join()
    print('end queue')
