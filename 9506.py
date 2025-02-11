result = []
while True:
    n = int(input())
    if n == -1:
        break

    case = []
    p = 0

    for i in range(1, n - 1):
        if n % i == 0:
            p += i
            case.append(i)

    if p == n:
        result.append((n, case))
    else:
        result.append((n, None))

for n, case in result:
    if case is None:
        print(f'{n} is NOT perfect.')
    else:
        print(f"{n} = {' + '.join(map(str, case))}")