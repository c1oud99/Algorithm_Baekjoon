import sys
from collections import deque

input = sys.stdin.read
data = input().splitlines()

queue = deque()
result = []

for line in data[1:]:
    order = line.split()
    if order[0] == "push":
        queue.append(int(order[1]))
    elif order[0] == "pop":
        result.append(queue.popleft() if queue else -1)
    elif order[0] == "size":
        result.append(len(queue))
    elif order[0] == "empty":
        result.append(0 if queue else 1)
    elif order[0] == "front":
        result.append(queue[0] if queue else -1)
    elif order[0] == "back":
        result.append(queue[-1] if queue else -1)

sys.stdout.write("\n".join(map(str, result)) + "\n")
