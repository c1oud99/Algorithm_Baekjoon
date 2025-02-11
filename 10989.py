import sys
input = sys.stdin.readline

N = int(input().strip())
count = [0] * 10001

for i in range(N):
    num = int(input().strip())
    count[num] += 1

for i in range(10001):
    if count[i] > 0:
        for _ in range(count[i]):
            print(i)