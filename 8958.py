N = int(input())
scores = []

for _ in range(N):
    case = input()
    cnt = 0
    score = 0
    for char in case:
        if char == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    scores.append(score)

for i in scores:
    print(i)