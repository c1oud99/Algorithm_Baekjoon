import numpy as np

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())  #
B = [list(map(int, input().split())) for _ in range(M)]

AB = np.dot(A, B)

for i in range(N):
    print(*AB[i])
