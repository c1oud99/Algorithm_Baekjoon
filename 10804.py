card = list(range(1,21))
for i in range(10):
    a, b = map(int, input().split())
    card[a-1:b] = card[a-1:b][::-1]
print(' '.join(map(str, card)))