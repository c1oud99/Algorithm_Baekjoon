N, M = map(int, input().split())
board = [input() for _ in range(N)]
result = []

for i in range(N - 7):
    for j in range(M - 7):
        W = 0
        B = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if board[a][b] != "W":
                        W += 1
                    if board[a][b] != "B":
                        B += 1
                else:
                    if board[a][b] != "B":
                        W += 1
                    if board[a][b] != "W":
                        B += 1
        result.append(W)
        result.append(B)

print(min(result))