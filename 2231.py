def result(N):
    for i in range(1, N + 1):
        num = i
        sum_digit = sum(map(int, str(i)))
        if num + sum_digit == N:
            return i
    return 0

N = int(input())
print(result(N))