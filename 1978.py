n = int(input())
count = 0
num = list(map(int, input().split()))

for i in range(n):
    if num[i] < 2:
        continue
    for j in range(2, num[i] + 1):
        if num[i] == j:
            count += 1
        if num[i] % j == 0:
            break

print(count);