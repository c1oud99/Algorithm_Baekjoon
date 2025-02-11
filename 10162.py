T = int(input())
A = 300
B = 60
C = 10

if T % C != 0:
    print(-1)
else:
    a = (T // A)
    b = ((T % A) // B)
    c = (((T % A) % B) // C)
    print(a, b, c)