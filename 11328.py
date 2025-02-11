for i in range(int(input())):
    first, second = input().split()
    if sorted(first) == sorted(second):
        print('Possible')
    else:
        print('Impossible')
