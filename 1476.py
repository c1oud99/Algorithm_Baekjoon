E, S, M = map(int, input().split())
e, s, m = 1, 1, 1
year = 1
while E != e or S != s or M != m:
    year += 1
    e = (year - 1) % 15 + 1
    s = (year - 1) % 28 + 1
    m = (year - 1) % 19 + 1
print(year)