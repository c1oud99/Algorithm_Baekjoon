for _ in range(3):
    count = sum(map(int, input().split()))
    if count == 3:
        print('A')
    elif count == 2:
        print('B')
    elif count == 1:
        print('C')
    elif count == 0:
        print('D')
    elif count == 4:
        print('E')
