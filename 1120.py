def is_prime(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime = False

    primes = [x for x in range(n + 1) if prime[x]]
    return primes

N = int(input())

