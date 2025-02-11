testcase = int(input())
case = [int(input()) for _ in range(testcase)]
for n in case:
    results = []
    for i in range(1, (n + 1) // 2):
        if i != (n - i):
            results.append((i, n - i))
    print(f"Pairs for {n}:", ', '.join(f"{a} {b}" for a, b in results))