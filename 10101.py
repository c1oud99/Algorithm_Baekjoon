t = [int(input()) for _ in range(3)]
if sum(t) != 180:
    print('Error')
elif all(num == 60 for num in t):
    print('Equilateral')
elif t[0] == t[1] or t[1] == t[2] or t[2] == t[0]:
    print('Isosceles')
else:
    print('Scalene')