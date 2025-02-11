def josephus(N, K):
    res = []
    line = [1 for _ in range(N)]
    i = -1
    for _ in range(N - 1):
        count = 0
        while count < K:
            i = (i + 1) % N
            if line[i]:
                count += 1
        line[i] = 0
        res.append(i + 1)
    res.append(line.index(1) + 1)
    return res

N, K = map(int, input().split())
result = josephus(N, K)

print('<', end='')
print(', '.join(map(str, result)), end='')
print('>')