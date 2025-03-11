N, M = map(int, input().split())
A = list(map(int, input().split()))
start, m, count = 0, 0, 0
for end in range(N):
    m += A[end]
    while m > M:
        m -= A[start]
        start += 1
    if m == M:
        count += 1
print(count)