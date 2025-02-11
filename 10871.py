N, X = map(int, input().split())
num = list(map(int, input().split()))
print(' '.join(str(n) for n in num if X > n))