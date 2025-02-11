N, K = map(int, input().split())
student = [[0, 0] for _ in range(6)]
for _ in range(N):
    S, Y = map(int, input().split())
    student[Y - 1][S] += 1

room = 0
for Y in range(6):
    for S in range(2):
        room += (student[Y][S] + K - 1)//K
print(room)