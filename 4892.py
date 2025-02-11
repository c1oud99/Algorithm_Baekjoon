result = []
while True:
    n0 = int(input())
    if n0 == 0:
        break
    n1 = 3 * n0
    if n1 % 2 == 0:
        n2 = n1 // 2
        outcome = 'even'
    else:
        n2 = (n1 + 1) // 2
        outcome = 'odd'
    n3 = 3 * n2
    result.append((outcome, n3 // 9))

for i, (outcome, n4) in enumerate(result, start = 1):
    print(f"{i}. {outcome} {n4}")