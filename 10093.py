A, B = map(int, input().split())
if A > B:
    A, B = B, A
result = [i for i in range(A + 1, B)]
print(len(result))
print(" ".join(map(str, result)))