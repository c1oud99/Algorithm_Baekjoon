X = int(input())
total = 0
cnt = 0
while total < X:
    cnt += 1
    total += cnt
pos = X - (total - cnt)
if cnt % 2 == 1:
    n, d = cnt - (pos - 1), pos
else:
    n, d = pos, cnt - (pos - 1)
print(f'{n}/{d}')