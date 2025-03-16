def is_prime(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False

    primes = [x for x in range(n + 1) if prime[x]]
    return primes

def three_primes(n):
    primes = is_prime(n)
    prime_set = set(primes)

    for i in range(len(primes)):
        for j in range(i, len(primes)):
            remain = n - primes[i] - primes[j]
            if remain in prime_set:
                return primes[i], primes[j], remain
    return 0

N = int(input())
for _ in range(N):
    print(*three_primes(int(input())))

