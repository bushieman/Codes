from timeit import default_timer as timer
import sys

start = timer()
numbers = []
for i in range(100):
    numbers.append(i)
stop = timer()
print(numbers)
print(stop-start)
print(sys.getsizeof(numbers))

