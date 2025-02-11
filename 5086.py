result = []
while True:
    A, B = map(int, input().split())
    if A == B == 0:
        break

    if B % A == 0:
        result.append('factor')
    elif A % B == 0:
        result.append('multiple')
    else:
        result.append('neither')

for i in result:
    print(i)