N, M = map(int, input().split())
s = {input() for _ in range(N)}
sum = 0
for i in range(M):
    if input() in s:
        sum += 1
print(sum)