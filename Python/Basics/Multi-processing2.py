from multiprocessing import Process, Value, Array
import os

def sqr():
    for i in range(100):
        i ** 2

if __name__ == '__main__':
    shared_number = Value('f', 0.43)
    print('Number at the beginning is', shared_number.value)
