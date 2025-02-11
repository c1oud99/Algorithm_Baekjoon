N = int(input())
divisors = []
for i in range(1, N + 1):
    if N % i == 0:
        divisors.append(i)

g = 0
for i in range(len(divisors)):
    g += sum(range(divisors[0], divisors[i]))

print(g)