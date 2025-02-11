T = int(input())
result = []
for _ in range(T):
    N = int(input())
    max_name = ""
    max_L = 0
    for _ in range(N):
        S, L = input().split()
        L = int(L)
        if L > max_L:
            max_name = S
            max_L = L
    result.append(max_name)

for i in result:
    print(i)