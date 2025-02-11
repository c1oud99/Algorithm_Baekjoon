T = int(input())
for _ in range(T):
    y_count = 0
    k_count = 0
    for _ in range(9):
        y, k = map(int, input().split())
        y_count += y
        k_count += k
    if y_count > k_count:
        print("Yonsei")
    elif y_count < k_count:
        print("Korea")
    else:
        print("Draw")
