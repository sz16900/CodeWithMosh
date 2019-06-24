# queues = FIFO (first in fitst out)

from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
# always check for empty lists
if not queue:
    print("empty!")
queue.popleft()
print(queue)
