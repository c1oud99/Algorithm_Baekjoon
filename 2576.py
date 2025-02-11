odd = [n for _ in range(7) if (n := int(input())) % 2 == 1]
if odd:
    print(sum(odd))
    print(min(odd))
else:
    print(-1)