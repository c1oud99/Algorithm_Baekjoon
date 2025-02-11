T = int(input())
v = [input().split() for _ in range(T)]

for i in range(T):
    n = float(v[i][0])
    for j in range(1, len(v[i])):
        if v[i][j] == '@':
            n *= 3
        elif v[i][j] == '%':
            n += 5
        elif v[i][j] == '#':
            n -= 7
    print(format(n, '.2f'))