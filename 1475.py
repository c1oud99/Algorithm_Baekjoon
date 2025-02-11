room = input().strip()
cnt = [0] * 10
for i in room:
    cnt[int(str(i))] += 1

cnt[6] = (cnt[6] + cnt[9] + 1) // 2
cnt[9] = cnt[6]

print(max(cnt))