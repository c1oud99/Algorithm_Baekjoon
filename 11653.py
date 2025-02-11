import math
N = int(input())
M = 2

while M <= int(math.sqrt(N)):
    if N % M != 0:
        M += 1
    else:
        N //= M
        print(M)

if N > 1:
    print(N)