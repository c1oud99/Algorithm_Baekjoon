def gcd(A, B):
    while B != 0:
        A, B = B, A % B
    return A

def lcm(A, B):
    return A * B // gcd(A, B)

T = int(input())
arr = [list(map(int, input().split())) for _ in range(T)]
for i in range(T):
    print(lcm(arr[i][0], arr[i][1]))


