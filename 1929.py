def find_primes(M, N):
    for i in range(M, N + 1):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0 and i % i == 0:
                count += 1
        if count == 2:
            print(i)

M, N = map(int, input().split())

find_primes(M, N)