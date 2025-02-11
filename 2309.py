from itertools import combinations
num = [int(input()) for _ in range(9)]
num.sort()
nine = sum(num)
for combo in combinations(num, 7):
    if sum(combo) == 100:
        print("\n".join(map(str, combo)))
        break