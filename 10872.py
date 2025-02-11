def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
N = int(input())
print(factorial(N))

'''
N = int(input())
result = 1
for i in range(1, N+1):
    result *= i
print(result)
'''