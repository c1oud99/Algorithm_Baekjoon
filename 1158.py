from collections import deque
N, K = map(int, input().split())
p = deque(range(1, N + 1))
result = []

while p:
    p.rotate(1 - K)
    result.append(p.popleft())
print('<'+', '.join(map(str, result))+'>')