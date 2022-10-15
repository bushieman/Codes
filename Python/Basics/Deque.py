from collections import deque

# creating
deque1 = deque('bushman', maxlen=15) # can take any iterable object as an argument

# useful methods
deque1.append(75)
deque1.appendleft('its')
deque1.pop()
deque1.popleft()
deque1.clear()
deque1.extend(['bushie', 'bushbaby', 'bushieman'])
deque1.extendleft('bush') # do not know the use case for this scenario
deque1.rotate(-1)
deque1.rotate(1)
deque1.reverse()
