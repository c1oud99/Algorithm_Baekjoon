result = []
while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    if A > B:
        result.append('Yes')
    else:
        result.append('No')

for i in result:
    print(i)