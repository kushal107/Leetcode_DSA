from collections import deque

queue = deque()

queue.append('a')
queue.append('4')

queue.popleft()

print(queue[0])
print(len(queue))
print(queue)