X = int(input())
Y = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    Y += a * b
if X == Y:
    print('Yes')
else:
    print('No')