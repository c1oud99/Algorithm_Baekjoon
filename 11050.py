N, K = map(int, input().split())

n, k, nk = 1, 1, 1
for a in range(1, N + 1):
    n *= a
for b in range(1, K + 1):
    k *= b
for c in range(1, N - K + 1):
    nk *= c

print(n // (k * nk))