from threading import Thread, Lock
import os
import time

def sqr():
    for i in range(100):
        i ** 2
        time.sleep(0.1)

threads = []
num_threads = 10

# create the processes
for _ in range(num_threads):
    t = Thread(target=sqr)
    threads.append(t)

# start the processes
for t in threads:
    t.start()

# joining - block the main thread until the threads are complete
for t in threads:
    t.join()
print('processes ended')


database_value = 0
def increase(lock):
    global database_value
    with lock:
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy
  

print('start threads', database_value)

# prevents run competition
lock = Lock()

# normal lock process
lock.acquire()
# some code...
lock.release()

# run competition occurs here
if __name__ == '__main__':
    lock = Lock()
    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase,  args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

print('end threads', database_value)
