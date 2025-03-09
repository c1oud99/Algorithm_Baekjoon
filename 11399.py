N = int(input())
P = sorted(list(map(int, input().split())))
c, t = 0, 0
for p in P:
    c += p
    t += c
print(t)