import sys
input = sys.stdin.readline

results = []

while True:
    sides = list(map(int, input().strip().split()))

    if sides == [0, 0, 0]:
        break

    sides.sort()
    a, b, c = sides

    if a ** 2 + b ** 2 == c ** 2:
        results.append("right")
    else:
        results.append("wrong")

for result in results:
    print(result)
