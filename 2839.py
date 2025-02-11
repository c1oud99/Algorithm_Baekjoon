def min(N):
    for i in range(N // 5, -1, -1):
        bags = N - i * 5
        if bags % 3 == 0:
            return i + (bags // 3)
    return -1

N = int(input().strip())

print(min(N))