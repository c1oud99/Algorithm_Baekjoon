import sys
from collections import deque
input = sys.stdin.readline

queue = deque()

n = int(input().strip())

for _ in range(n):
    command = input().strip()

    if command.startswith('push'):
        _, num = command.split()
        queue.append(int(num))
    elif command == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        print(1 if not queue else 0)
    elif command == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
