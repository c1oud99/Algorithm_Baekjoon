N = int(input())
result = []

for i in range(N):
    dice = list(map(int, input().split()))
    dice.sort()
    if dice[0] == dice[1] == dice[2]:
        result.append(10000 + dice[0] * 1000)
    elif dice[0] == dice[1] or dice[1] == dice[2]:
        result.append(1000 + dice[1] * 100)
    else:
        result.append(dice[2] * 100)

print(max(result))

