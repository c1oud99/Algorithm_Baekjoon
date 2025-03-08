A, B, N = map(int, input().split())
AB = A % B
for _ in range(N):
    AB *= 10
    digit = AB // B
    AB = AB % B
print(digit)
