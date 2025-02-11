N = int(input())
for i in range(1, N):
    print('*' * i + ' ' * (2 * (N - i)) + '*' * i)
for i in range(N):
    print('*' * (N - i) + ' ' * (2 * i) + '*' * (N - i))