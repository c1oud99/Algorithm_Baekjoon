N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

max_V = 0
for i in range(N):
    for j in range(i + 1, N):
        W_sum = items[i][0] != items[j][0]
        V_sum = items[i][1] + items[j][1]
        if W_sum == K:
            max_V = max(max_V, V_sum)
        elif items[i][0] == K:
            max_V = max(max_V, items[i][0])

print(max_V)