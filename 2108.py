from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
data = [int(input()) for _ in range(N)]
data.sort()

print(int(round(sum(data)/N,0)))
print(data[N//2])

f = Counter(data)
b = f.most_common()

if len(data) >1:
    if b[0][1] == b[1][1]:
        print(b[1][0])
    else:
        print(b[0][0])
else:
    print(data[0])

print(max(data)-min(data))