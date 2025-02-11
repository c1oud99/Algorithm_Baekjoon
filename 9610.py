n = int(input())
counts = [0, 0, 0, 0, 0]
for _ in range(n):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        counts[0] += 1
    elif x < 0 and y > 0:
        counts[1] += 1
    elif x < 0 and y < 0:
        counts[2] += 1
    elif x > 0 and y < 0:
        counts[3] += 1
    else:
        counts[4] += 1

print('Q1: '+ str(counts[0]))
print('Q2: '+ str(counts[1]))
print('Q3: '+ str(counts[2]))
print('Q4: '+ str(counts[3]))
print('AXIS: '+ str(counts[4]))

