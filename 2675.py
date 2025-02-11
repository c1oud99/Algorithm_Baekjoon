T = int(input())
case = [input().split() for _ in range(T)]

for i in range(T):
    R = int(case[i][0])
    for j in range(len(case[i][1])):
        print(case[i][1][j] * int(R), end = '')
    print('')
